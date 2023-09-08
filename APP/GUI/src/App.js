import React from 'react';
import './App.scss';
import { Content, Theme } from '@carbon/react';
import { Route, Switch, BrowserRouter } from 'react-router-dom';

import AppHeader from './components.en/AppHeader';

import LandingPage from './content.en/LandingPage';
import DemoRagPage from './content.en/DemoRagPage';

function App() {
  return (
    <>
      <BrowserRouter>
        <Theme theme="white">
          <AppHeader />
        </Theme>
        <Content>
          <Switch>
            <Route exact path="/" component={LandingPage} />
            <Route exact path="/demoRAG" component={DemoRagPage} />
          </Switch>
        </Content>
      </BrowserRouter>
    </>
  );
}

export default App;
