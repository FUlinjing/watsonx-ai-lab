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
        <h1 className="landing-page__heading">Discover the new generation of artificial intelligence</h1>
      </Column>

      <Column lg={16} md={8} sm={4} className="landing-page__r2">
        <Tabs defaultSelectedIndex={0}>
          <TabList className="tabs-group" aria-label="Tab navigation">
            <Tab>Welcome</Tab>
            <Tab>Agenda</Tab>
            <Tab>Demonstrations</Tab>
          </TabList>
          <TabPanels>
            <TabPanel>
              <Grid className="tabs-group-content">
                <Column md={4} lg={7} sm={4} className="landing-page__tab-content">
                  <h2 className="landing-page__subheading">We warmly welcome you.</h2>
                  <p className="landing-page__p">
                    Welcome to the workshops <span style={{ fontWeight: 'bold' }}>„watsonx - discover the new generation of artificial intelligence”</span>. This is a unique event, a great opportunity to get to know our latest solution in the field of generative artificial intelligence - the <span style={{ fontWeight: 'bold' }}>watsonx</span> platform, as well as business strategies related to its use.
                  </p>
                  <Button href="https://www.ibm.com/events/reg/flow/ibm/yh7o28mb/landing/page/landing">Registration</Button>
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
                  <h2 className="landing-page__subheading">Hourly plan of lectures.</h2>
                  <p className="landing-page__p">
                    <table>
                      <tr><td>10:10</td><td>-</td><td>10:30</td><td style={{paddingLeft: '15px'}}> Challenges facing clients and partners from IBM's perspective</td></tr>
                      <tr><td>10:30</td><td>-</td><td>11:30</td><td style={{paddingLeft: '15px'}}> Introduction to generative artificial intelligence and the watsonx platform</td></tr>
                      <tr><td>10:30</td><td>-</td><td>10:50</td><td style={{paddingLeft: '15px'}}> watsonx - IBM platform in the field of generative artificial intelligence</td></tr>
                      <tr><td>10:30</td><td>-</td><td>10:50</td><td style={{paddingLeft: '15px'}}> watsonx.ai</td></tr>
                      <tr><td>10:50</td><td>-</td><td>11:10</td><td style={{paddingLeft: '15px'}}> watsonx.data</td></tr>
                      <tr><td>11:10</td><td>-</td><td>11:30</td><td style={{paddingLeft: '15px'}}> watsonx.governance</td></tr>
                      <tr><td>11:30</td><td>-</td><td>12:00</td><td style={{paddingLeft: '15px'}}> Example use cases</td></tr>
                      <tr><td>12:00</td><td>-</td><td>12:30</td><td style={{paddingLeft: '15px'}}> How to commercialize watsonx?</td></tr>
                      <tr><td>12:30</td><td>-</td><td>13:00</td><td style={{paddingLeft: '15px'}}> Q&A</td></tr>
                      <tr><td>13:00</td><td>-</td><td>14:00</td><td style={{paddingLeft: '15px'}}> Lunch</td></tr>
                      <tr><td>14:00</td><td>-</td><td>16:00</td><td style={{paddingLeft: '15px'}}> Technical workshops</td></tr>
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
                  <h2 className="landing-page__subheading">Examples of using Large Language Models</h2>
                  <p className="landing-page__p">
                    <table>
                      <tr><td><p>
                        <Link to="/demoRAG">Demo1</Link>
                        </p></td><td style={{paddingLeft: '15px'}}><p>Using Large Language Models to generate more accurate answers based on information contained in a specified set of unstructured data. In the demo, the set of unstructured data is a set of PDF files with amendments to the EU AI Act provided by the European Union. In the demo application, you can ask any question about the content of the "EU AI Act" document, and the application will find text fragments that are most likely to contain an answer to the question using IBM Watson Discovery, and then the language model from IBM Watsonx will create a concise answer to the question based on these text fragments.</p></td></tr>
                      <tr><td><p><a href="https://ai-for-business-iis-web.wdc1a.cirrus.ibm.com/showcase/claim-evaluation">Demo2</a></p></td><td style={{paddingLeft: '15px'}}><p>Using Large Language Models to extract information from any text written in natural language. The demo application analyzes the description of a road accident that every victim should provide to the insurance company. This description can be entered in any form. The demo application will automatically find information about the location of the accident and the registration numbers of the vehicles involved in the accident. If this information is not provided, the application will inform about the need to add this data to the accident description.</p></td></tr>
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
            <h3 className="landing-page__label">We are here for you</h3>
          </Column>
          <Column md={4} lg={4} sm={4}>
            Our team
          </Column>
          <Column md={4} lg={4} sm={4}>
            Useful resources
          </Column>
          <Column md={4} lg={4} sm={4}>
            Participation rules
          </Column>
        </Grid>
      </Column>
    </Grid>
  );
};

export default LandingPage;
