import React from 'react';
import { useState, useCallback } from 'react';
import { WebChatContainer} from '@ibm-watson/assistant-web-chat-react';
import { CheckmarkOutline} from '@carbon/icons-react';
import { Table, TableHead, TableRow, TableHeader, TableBody, TableCell} from '@carbon/react';
import sourcePDF from "./AI ACT PL.pdf";
import {
  Breadcrumb,
  BreadcrumbItem,
  Button,
  Tabs,
  Tab,
  TabList,
  TabPanels,
  TabPanel,
  Grid,
  Column,
  InlineLoading,
  Heading,
  Section,
  Search,
  ToastNotification,
} from '@carbon/react';
import moment from "moment";

import { env } from "../../components/AppConfig/env"

const webChatOptions = {
  integrationID: env.REACT_APP_WA_INTEGRATIONID, //  The ID of this integration.
  region: env.REACT_APP_WA_REGION, // The region your integration is hosted in.
  serviceInstanceID: env.REACT_APP_WA_SERVICEINSTANCEID, // The ID of your service instance.
};

const DemoRagPage = () => {
  
  let [question, setQuestion] = useState();
  const [resAnswer, setResAnswer] = useState();
  const [resQuestion, setResQuestion] = useState();
  const [resSource, setResSource] = useState([]);
  let [isAnswered, setIsAnswered] = useState(false);
  let [isLoading, setIsLoading] = useState(false);
  let [isError, setIsError] = useState(false);
  let [errorMessage, setErrorMessage] = useState("Błąd");
  let [time, setTime] = useState();
  let [showNotification, setShowNotification] = useState(false);
  let num = "";
  
  const onBeforeRender = useCallback((instance) => {
    const customLanguagePack = {
      "input_placeholder": "Wprowadź tekst...",
    };
    instance.updateLanguagePack(customLanguagePack);
  }, [])

  const handleText = (event) => {
    setQuestion(event.target.value)
  };

  function nextQuestion(){
    setQuestion("")
    setIsAnswered(false)
  }

  function raiseNotification(){
    setTime(moment().format('HH:mm:ss DD.MM.yyyy').toString())
    setShowNotification(true)
  }

  function sendRequest(){
    setIsLoading(true)
    setIsError(false)
    
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    myHeaders.append("X-API-Key", env.REACT_APP_BE_APIKEY );

    var raw = JSON.stringify({
      "question": question
    });

    var requestOptions = {
      method: 'POST',
      mode: 'cors',
      headers: myHeaders,
      body: raw,
      redirect: 'follow'
    };
    var resp;
    fetch(env.REACT_APP_BE_APIURL, requestOptions)
      .then(response => 
        {
          resp = response;
          return response.json();
        })
      .then(result =>
        {
          console.log("Response: ", result)
          if (!resp.ok)
          {
            setIsError(true)
            setIsLoading(false)
            setErrorMessage("Brak pytania")
            raiseNotification()
          }
          else if (result['answer']==='')
          {
            setIsError(true)
            setIsLoading(false)
            setErrorMessage("Upłynął czas na odpowiedź z serwera")
            raiseNotification()
          }
          else
          {
            setResAnswer(result['answer'])
            setResQuestion(result['question'])
            setResSource(result['source'])
            setIsLoading(false)
            setIsAnswered(true)
            setShowNotification(false)
          }
        })
      .catch(error => {
        setIsError(true)
        console.log('Error: ', error)}
        );
  }
  
  return <Grid className="landing-page" fullWidth>
    <Column lg={16} md={8} sm={4} className="landing-page__banner">
      <Breadcrumb noTrailingSlash aria-label="Page navigation">
        <BreadcrumbItem>
          <a href="https://www.ibm.com/partnerplus">Partner Plus</a>
        </BreadcrumbItem>
      </Breadcrumb>
      <h1 className="landing-page__heading landing-page__heading_accent">WATSONX</h1>
      <h1 className="landing-page__heading">Okryj nową generację sztucznej inteligencji</h1>

      {showNotification &&
        <ToastNotification
            aria-label="closes notification"
            caption={time}
            onClose={() => { setShowNotification(false)}}
            onCloseButtonClick={() => { setShowNotification(false)}}
            statusIconDescription="notification"
            subtitle={errorMessage}
            title="Błąd przetwarzania"
            style={{zIndex: 1, float: 'right', position: 'absolute', top: 10, right: 1}}
          />
        }
    </Column>

    <Column lg={16} md={8} sm={4} className="landing-page__r2">
      <Tabs defaultSelectedIndex={0}>
        <TabList className="tabs-group" aria-label="Tab navigation">
          <Tab>Formularz</Tab>
          <Tab>Instrukcja</Tab>
        </TabList>
        <TabPanels>
          <TabPanel className={[isAnswered && 'background_change']} >
            <Grid className="tabs-group-content" >
              <Column md={4} lg={8} sm={4} className="landing-page__tab-content">
                {isAnswered===false && <div className='question_box'>
                  
                  <Section level={3}><Heading>Pytania do dokumentacji</Heading></Section>
                  <div className="container_question">
                    <Search className="question_input" size="lg" placeholder="Napisz swoje pytanie..." labelText="Search" closeButtonLabelText="" id="text-input" onChange={handleText} />
                    <Button className="question_button" onClick={sendRequest}>Wyszukaj</Button>
                    {isLoading && <InlineLoading status="active" iconDescription="Loading" description="Przetwarzanie..."/>}
                    {isError && <InlineLoading status="error" iconDescription="Loading" description={errorMessage}/>}
                  </div>
                  </div>
                }
              </Column>

              <Column md={4} lg={{ span: 9, offset: 9 }} sm={4}>
                {isAnswered===false && <div><center>
                    <img className="img_watsonx"
                    src={`${process.env.PUBLIC_URL}/tab-ragdemo.png`}
                    alt="Watsonx illustration"/></center>
                  </div>
                }
              </Column>
            </Grid>

            {isAnswered && <div>
              <div className='above_table'>
                <h5 className='answer_area'><h3>{resQuestion}</h3></h5> 
                <Button className='bottomContainer' kind="ghost" onClick={nextQuestion}>Zadaj kolejne pytanie</Button> 
              </div>
              <div className='answer_area'>
                <div><h4 className='answer_text'><CheckmarkOutline style={{ color: "green" }}/> {resAnswer}</h4></div>
              </div>
              <div className='above_table'>
                <h5 className='answer_area'>Gdzie znaleźć więcej informacji na ten temat?</h5> 
              </div>

              <Table size="lg" useZebraStyles={false} className='answer_table'>
                <TableHead style={{height: 40}}>
                  <TableHeader style={{width: 150}}>
                    Nazwa pliku
                  </TableHeader>
                  <TableHeader style={{width: 100}}>
                    Strony
                  </TableHeader>
                  <TableHeader>
                    Tekst
                  </TableHeader>
                </TableHead>
                <TableBody>
                  {resSource.map((item, i) => {
                    return [
                      <TableRow key={i}>
                        <TableCell><a href={sourcePDF} target="_blank"
                            rel="noreferrer">
                            {item.filename}</a></TableCell>
                        {item.pages.map((items, j) => {
                            num = num + items + ", "
                            return null
                          })}
                        <TableCell>{num.slice(0, -2)}</TableCell>
                        {num = ""}
                        <TableCell style={{paddingBottom: 8, paddingTop: 8}}>{item.text}</TableCell>
                      </TableRow>
                    ];
                  })}
                </TableBody>
              </Table>
            </div>}
          </TabPanel>

          <TabPanel className='background_change'>
            <Grid className="tabs-group-content">
              <Column lg={16} md={8} sm={4} className="landing-page__tab-content">
                Instrukcja {env.REACT_APP_WA_REGION}
              </Column>
            </Grid>
          </TabPanel>
        </TabPanels>
      </Tabs>
    </Column>
  <WebChatContainer config={webChatOptions} onBeforeRender={onBeforeRender}/>
</Grid>;
};

export default DemoRagPage;
