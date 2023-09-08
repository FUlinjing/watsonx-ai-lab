import React from 'react';
import { Link } from 'react-router-dom';

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
} from '@carbon/react';

const LandingPage = () => {
  return (
    <Grid className="landing-page" fullWidth>
      <Column lg={16} md={8} sm={4} className="landing-page__banner">
        <Breadcrumb noTrailingSlash aria-label="Page navigation">
          <BreadcrumbItem>
            <a href="https://www.ibm.com/partnerplus">Partner Plus</a>
          </BreadcrumbItem>
        </Breadcrumb>
        <h1 className="landing-page__heading landing-page__heading_accent">WATSONX</h1>
        <h1 className="landing-page__heading">Okryj nową generację sztucznej inteligencji</h1>
      </Column>

      <Column lg={16} md={8} sm={4} className="landing-page__r2">
        <Tabs defaultSelectedIndex={0}>
          <TabList className="tabs-group" aria-label="Tab navigation">
            <Tab>Witamy</Tab>
            <Tab>Agenda</Tab>
            <Tab>Demonstracje</Tab>
          </TabList>
          <TabPanels>
            <TabPanel>
              <Grid className="tabs-group-content">
                <Column md={4} lg={7} sm={4} className="landing-page__tab-content">
                  <h2 className="landing-page__subheading">Serdecznie Państwa witamy.</h2>
                  <p className="landing-page__p">
                    Witamy na warsztatach <span style={{ fontWeight: 'bold' }}>„watsonx - okryj nową
                      generację sztucznej inteligencji”</span>. Jest to wyjątkowe wydarzenie, będące
                    świetną okazją do poznania naszego najnowszego rozwiązania w dziedzinie
                    generatywnej sztucznej inteligencji - platformy <span style={{ fontWeight: 'bold' }}>watsonx</span>, a także strategii
                    biznesowych związanych z jej wykorzystaniem.
                  </p>
                  <Button href="https://www.ibm.com/events/reg/flow/ibm/yh7o28mb/landing/page/landing">Rejestracja</Button>
                </Column>
                <Column md={4} lg={{ span: 8, offset: 7 }} sm={4}>
                  <img
                    className="landing-page__illo"
                    src={`${process.env.PUBLIC_URL}/tab-illo.png`}
                    alt="Watsonx illustration"
                  />
                </Column>
              </Grid>
            </TabPanel>
            <TabPanel>
              <Grid className="tabs-group-content">
                <Column md={4} lg={7} sm={4} className="landing-page__tab-content">
                  <h2 className="landing-page__subheading">Godzinny rozpoczęcia prelekcji.</h2>
                  <p className="landing-page__p">
                    <table>
                      <tr><td>10:10</td><td>-</td><td>10:30</td><td style={{paddingLeft: '15px'}}> Wyzwania stojące przed klientami i partnerami z perspektywy IBM</td></tr>
                      <tr><td>10:30</td><td>-</td><td>11:30</td><td style={{paddingLeft: '15px'}}> Wprowadzenie do generatywnej sztucznej inteligencji oraz platformy watsonx</td></tr>
                      <tr><td>10:30</td><td>-</td><td>10:50</td><td style={{paddingLeft: '15px'}}> watsonx - platforma IBM w obszarze generatywnej sztucznej inteligencji</td></tr>
                      <tr><td>10:30</td><td>-</td><td>10:50</td><td style={{paddingLeft: '15px'}}> watsonx.ai</td></tr>
                      <tr><td>10:50</td><td>-</td><td>11:10</td><td style={{paddingLeft: '15px'}}> watsonx.data</td></tr>
                      <tr><td>11:10</td><td>-</td><td>11:30</td><td style={{paddingLeft: '15px'}}> watsonx.governance</td></tr>
                      <tr><td>11:30</td><td>-</td><td>12:00</td><td style={{paddingLeft: '15px'}}> Przykładowe przypadki użycia</td></tr>
                      <tr><td>12:00</td><td>-</td><td>12:30</td><td style={{paddingLeft: '15px'}}> Jak skomercjalizować watsonx?</td></tr>
                      <tr><td>12:30</td><td>-</td><td>13:00</td><td style={{paddingLeft: '15px'}}> Q&A</td></tr>
                      <tr><td>13:00</td><td>-</td><td>14:00</td><td style={{paddingLeft: '15px'}}> Lunch</td></tr>
                      <tr><td>14:00</td><td>-</td><td>16:00</td><td style={{paddingLeft: '15px'}}> Warsztaty techniczne</td></tr>
                    </table>
                  </p>
                </Column>
                <Column md={4} lg={{ span: 8, offset: 7 }} sm={4}>
                  <img
                    className="landing-page__illo"
                    src={`${process.env.PUBLIC_URL}/tab-illo2.png`}
                    alt="Watsonx illustration"
                  />
                </Column>
              </Grid>
            </TabPanel>
            <TabPanel>
              <Grid className="tabs-group-content">
              <Column md={4} lg={7} sm={4} className="landing-page__tab-content">
                  <h2 className="landing-page__subheading">Przykłady użycia Dużych Modeli Językowych</h2>
                  <p className="landing-page__p">
                    <table>
                      <tr><td><p>
                        <Link to="/demoRAG">Demo1</Link>
                        </p></td><td style={{paddingLeft: '15px'}}><p>Wykorzystanie Dużych Modeli Językowych do generowania bardziej trafnych odpowiedzi, które są 
                                                                          oparte na informacjach zawartych w wskazanym zbiorze danych nieustrukturyzowanych.</p>
                                                                          <p>W demo zbiorem danych nieustrukutyzowanych jest zestaw plików PDF z poprawkami do EU AI Act
                                                                             udostępnionymi przez Unię Europejską.</p>
                                                                             <p>W aplikacji demo możesz zadać dowolne pytanie do zawartości dokumentu "EU AI Act", a aplikacja odnajdzie fragmenty tekstów
                                                                              które z najwyższym prawdopodobieństwem zawierają odpowiedź na pytanie wykorzystując IBM Watson Discovery
                                                                              , a następnie model językowy z IBM Watsonx na podstawie tych fragmentów tekstów stworzy zwięzłą odpowiedź na stawiane pytanie.</p><br></br>
                                                </td></tr>
                      <tr><td><p><a href="https://ai-for-business-iis-web.wdc1a.cirrus.ibm.com/showcase/claim-evaluation">Demo2</a></p></td><td style={{paddingLeft: '15px'}}><p>Wykorzystanie Dużych Modeli Językowych do pozyskania informacji z dowolnego tekstu napisanego w języku naturalnym </p>
                                                                            <p>Aplikacja demo, analizuje opis zdarzenia drogowego, jaki każdy poszkodowany powinien przedstawić firmie ubezpieczeniowej. Opis
                                                                              ten może być wprowadzony w dowolnej formie. Aplikacja demo automatycznie odszuka informacje dotyczące miejsca zdarzenia i 
                                                                              numerów rejestracyjnych pojazdów uczestniczących w zdarzeniu. Jeżeli informacje te nie są podane, to aplikacja poinformuje 
                                                                              o konieczności dopisania tych danych do opisu zdarzenia.</p></td></tr>
                    </table>
                  </p>
                </Column>
                <Column md={4} lg={{ span: 8, offset: 7 }} sm={4}>
                  <img
                    className="landing-page__illo"
                    src={`${process.env.PUBLIC_URL}/tab-illo.png`}
                    alt="Watsonx illustration"
                  />
                </Column>
              </Grid>
            </TabPanel>
          </TabPanels>
        </Tabs>
      </Column>
      <Column lg={16} md={8} sm={4} className="landing-page__r3">
        <Grid>
          <Column md={4} lg={4} sm={4}>
            <h3 className="landing-page__label">Jesteśmy tu dla Was</h3>
          </Column>
          <Column md={4} lg={4} sm={4}>
            Nasz zespół
          </Column>
          <Column md={4} lg={4} sm={4}>
            Przydatne zasoby
          </Column>
          <Column md={4} lg={4} sm={4}>
            Zasady uczestnictwa
          </Column>
        </Grid>
      </Column>
    </Grid>
  );
};

export default LandingPage;