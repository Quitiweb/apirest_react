import React, { useState, useEffect } from "react";
// react plugin for creating charts
import ChartistGraph from "react-chartist";
// @material-ui/core
import { makeStyles } from "@material-ui/core/styles";
import Icon from "@material-ui/core/Icon";
// @material-ui/icons
import Store from "@material-ui/icons/Store";
import Warning from "@material-ui/icons/Warning";
import DateRange from "@material-ui/icons/DateRange";
import LocalOffer from "@material-ui/icons/LocalOffer";
import Update from "@material-ui/icons/Update";
import ArrowUpward from "@material-ui/icons/ArrowUpward";
import AccessTime from "@material-ui/icons/AccessTime";
import Accessibility from "@material-ui/icons/Accessibility";
import InvertColorsIcon from '@material-ui/icons/InvertColors';
import WhatshotIcon from '@material-ui/icons/Whatshot';
import AcUnitIcon from '@material-ui/icons/AcUnit';
import BugReport from "@material-ui/icons/BugReport";
import Code from "@material-ui/icons/Code";
import Cloud from "@material-ui/icons/Cloud";
// core components
import GridItem from "components/Grid/GridItem.js";
import GridContainer from "components/Grid/GridContainer.js";
import Table from "components/Table/Table.js";
import Tasks from "components/Tasks/Tasks.js";
import CustomTabs from "components/CustomTabs/CustomTabs.js";
import Danger from "components/Typography/Danger.js";
import Card from "components/Card/Card.js";
import CardHeader from "components/Card/CardHeader.js";
import CardIcon from "components/Card/CardIcon.js";
import CardBody from "components/Card/CardBody.js";
import CardFooter from "components/Card/CardFooter.js";

import axios from 'axios';

import { bugs, website, server } from "variables/general.js";

import {
  dailySalesChart,
  emailsSubscriptionChart,
  completedTasksChart
} from "variables/charts.js";

import styles from "assets/jss/material-dashboard-react/views/dashboardStyle.js";

const useStyles = makeStyles(styles);

export default function Dashboard() {

  const [username, setUsername] = useState(localStorage.getItem('username') ? localStorage.getItem('username') : null);
  const [token, setToken] = useState(localStorage.getItem('token') ? localStorage.getItem('token') : null);

  const [devices, setDevices] = useState([]);
  const [tempMax, setTempMax] = useState([]);
  const [tempMin, setTempMin] = useState([]);
  const [tempAmb, setTempAmb] = useState([]);
  const [tempOil, setTempOil] = useState([]);

  var array = []
  
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/', { headers: { "Authorization": token } })
      .then(function (response) {

        for(var i in response.data) {
            array.push(
              [response.data[i]['id'], 
              response.data[i]['name'],
              response.data[i]['configuration'] ? response.data[i]['configuration'] : '---',
              response.data[i]['remoteLog'] ? 'true' : 'false',
              response.data[i]['MACAddress']
            ]);
        }
        setDevices(array);
      })
      .catch(function (error) {
        console.log(error)
      });

      axios.get('http://127.0.0.1:8000/log', { headers: { "Authorization": token } })
          .then(function (response) {
    
            for(var i in response.data) {
                let datos = response.data[i]['data'].split(",");
                let arrayDatos = []
                for(var j in datos) {
                    arrayDatos.push(datos[j])
                }
                setTempMax(datos[1]);
                setTempMin(datos[2]);
                setTempAmb(datos[3]);
                setTempOil(datos[4]);
                
            }
            
          })
          .catch(function (error) {
            console.log(error)
          });
  }, []);


  const classes = useStyles();
  return (
    username ? // operador ternario para mostrar la info o no
      <div>
        <GridContainer>
          <GridItem xs={12} sm={6} md={3}>
            <Card>
              <CardHeader color="warning" stats icon>
                <CardIcon color="warning">
                  <WhatshotIcon/>
                </CardIcon>
                <p className={classes.cardCategory}>Max temp</p>
                <h3 className={classes.cardTitle}>
                  {tempMax} <small>º</small>
                </h3>
              </CardHeader>
              <CardFooter stats>
                <div className={classes.stats}>
                  <Icon>info_outline</Icon>
                  <a href="logs">
                    View more detailed info
                  </a>
                </div>
              </CardFooter>
            </Card>
          </GridItem>
          <GridItem xs={12} sm={6} md={3}>
            <Card>
              <CardHeader color="success" stats icon>
                <CardIcon color="success">
                  <AcUnitIcon/>
                </CardIcon>
                <p className={classes.cardCategory}>Min temp</p>
                <h3 className={classes.cardTitle}>{tempMin} <small>º</small></h3>
              </CardHeader>
              <CardFooter stats>
                <div className={classes.stats}>
                
                  <Icon>info_outline</Icon>
                  
                  <a href="logs">
                    View more detailed info
                  </a>
                </div>
              </CardFooter>
            </Card>
          </GridItem>
          <GridItem xs={12} sm={6} md={3}>
            <Card>
              <CardHeader color="danger" stats icon>
                <CardIcon color="danger">
                  <Icon>info_outline</Icon>
                </CardIcon>
                <p className={classes.cardCategory}>Amb temp</p>
                <h3 className={classes.cardTitle}> {tempAmb} <small>º</small></h3>
              </CardHeader>
              <CardFooter stats>
                <div className={classes.stats}>
                <Icon>info_outline</Icon>
                  
                  <a href="logs">
                    View more detailed info
                  </a>
                </div>
              </CardFooter>
            </Card>
          </GridItem>
          <GridItem xs={12} sm={6} md={3}>
            <Card>
              <CardHeader color="info" stats icon>
                <CardIcon color="info">
                  <InvertColorsIcon />
                </CardIcon>
                <p className={classes.cardCategory}>Oil temp</p>
                <h3 className={classes.cardTitle}> {tempOil} <small>º</small></h3>
              </CardHeader>
              <CardFooter stats>
                <div className={classes.stats}>
                <Icon>info_outline</Icon>
                  
                  <a href="logs">
                    View more detailed info
                  </a>
                </div>
              </CardFooter>
            </Card>
          </GridItem>

          {/* tabla principal */}
          <GridItem xs={12} sm={12} md={12}>
            <Card plain>
              <CardHeader plain color="primary" style={{ background: '#00796b' }}>
                <h4 className={classes.cardTitleWhite}>
                  Devices List
            </h4>
                <p className={classes.cardCategoryWhite}>

                </p>
              </CardHeader>
              <CardBody>
                <Table
                  tableHeaderColor="primary"
                  tableHead={["ID", "Name", "Configuration", "remoteLog", "MACAddress"]}
                  tableData={devices}
                />
              </CardBody>
            </Card>
          </GridItem>
        </GridContainer>
      </div>

      :

      <div>
        <GridContainer>
          <GridItem xs={12} style={{ textAlign: "center" }}>
            <h2>Please, log in to check your devices' information</h2>
          </GridItem>
        </GridContainer>
      </div>
  );
}
