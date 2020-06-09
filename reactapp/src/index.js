/*!

=========================================================
* Material Dashboard React - v1.8.0
=========================================================

* Product Page: https://www.creative-tim.com/product/material-dashboard-react
* Copyright 2019 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/material-dashboard-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import React from "react";
import ReactDOM from "react-dom";
import { createBrowserHistory } from "history";
import { createMemoryHistory } from "history";
import { Router, Route, Switch, Redirect } from "react-router-dom";

// core components
import Admin from "layouts/Admin.js";
import RTL from "layouts/RTL.js";


import "assets/css/material-dashboard-react.css?v=1.8.0";

const memoryHistory = createMemoryHistory();

// const hist = createBrowserHistory();

window.$BASE_URL = 'http://127.0.0.1:8000';
// window.$BASE_URL = 'https://qw-django.club';

ReactDOM.render(
  <Router history={memoryHistory}>
    <Switch>
      <Route path="" component={Admin} />
    </Switch>
  </Router>,
  document.getElementById("root")
);
