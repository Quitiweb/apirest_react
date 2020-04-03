import React, { useState, useEffect }  from 'react'
import GridContainer from "components/Grid/GridContainer";
import GridItem from "components/Grid/GridItem.js";
import Card from "components/Card/Card.js";
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import MenuItem from '@material-ui/core/MenuItem';
import CardHeader from "components/Card/CardHeader.js";
import CardIcon from "components/Card/CardIcon.js";
import CardBody from "components/Card/CardBody.js";
import CardFooter from "components/Card/CardFooter.js";
import Table from "components/Table/Table.js";
import { makeStyles } from "@material-ui/core/styles";
import styles from "assets/jss/material-dashboard-react/components/tableStyle.js";
import axios from 'axios';

const useStyles = makeStyles(styles);


export default function TablaLogs() {
    const classes = useStyles();

    const [username, setUsername] = useState(localStorage.getItem('username') ? localStorage.getItem('username') : null);
    const [token, setToken] = useState(localStorage.getItem('token') ? localStorage.getItem('token') : null);
    const [devices, setDevices] = useState([]);

    const [logs, setLogs] = useState([]);

    const [filterValue, setFilterValue] = useState(0);

    var array = []
    var arrayDevices = []

    useEffect(() => {

      axios.get('http://127.0.0.1:8000/', { headers: { "Authorization": token} }) // "user": token
      .then(function (response) {                                             // en user se puede introducir un token
          console.log(response.data)                                          // de la BBDD para acceder a la info de otro user.
        for(var i in response.data) {
            arrayDevices.push(
              [response.data[i]['id'], 
              response.data[i]['name'],
            ]);
        }
        setDevices(arrayDevices);
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
              console.log(arrayDatos)
              array.push([response.data[i]['timestamp'], response.data[i]['device'], datos[1], datos[2], datos[3], datos[4],datos[5], datos[6], datos[7], datos[8], datos[9], datos[10], datos[11]]);
          }
          setLogs(array);
        })
        .catch(function (error) {
          console.log(error)
        });
    }, []);

  const handleChange = (event) => {
    setFilterValue(event.target.value);
    axios.get('http://127.0.0.1:8000/log', { headers: { "Authorization": token, 'device': event.target.value } })
    .then(function (response) {

      for(var i in response.data) {
          let datos = response.data[i]['data'].split(",");
          let arrayDatos = []
          for(var j in datos) {
              arrayDatos.push(datos[j])
          }

          array.push([response.data[i]['timestamp'], response.data[i]['device'], datos[1], datos[2], datos[3], datos[4],datos[5], datos[6], datos[7], datos[8], datos[9], datos[10], datos[11]]);
      }
      setLogs(array);    
    })
    .catch(function (error) {
      console.log(error)
    });
  };


    return (
        username ? // operador ternario para mostrar la info o no

        <GridContainer>
          <GridItem xs={12} style={{ marginBottom: 15 }}>
            <span style={{ marginRight: 15, position: 'relative', top: 5 }}>Select device</span>
            <FormControl variant="outlined">
              <Select labelId="label" id="select" value={filterValue} onChange={handleChange}>
                <MenuItem value={0}>All</MenuItem>
                {devices.map((item, index) => (
                  <MenuItem value={item[0]}>{item[1]}</MenuItem>
                ))}
              </Select>
            </FormControl>
          </GridItem>

            {/* tabla principal */}
            <GridItem xs={12} sm={12} md={12}>
                <Card plain>
                <CardHeader plain color="primary" style={{ background: '#00796b' }}>
                    <h4 className={classes.cardTitleWhite}>
                    Recent logs
                </h4>
                    <p className={classes.cardCategoryWhite}>

                    </p>
                </CardHeader>
                <CardBody>
                    <Table
                    tableHeaderColor="primary"
                    tableHead={["Date", "Device", "Temp upper", "Temp lower", "Temp Amb", "Temp Oil", "PressureDie", "PressurePump", "Scale1", "Scale2", "Scale3", "Mode", "Freq"]}
                    tableData={logs}
                    />
                </CardBody>
                </Card>
            </GridItem>
        </GridContainer>

      :
      
      <div>
        <GridContainer>
          <GridItem xs={12} style={{ textAlign: "center" }}>
            <h2>Please, log in to check your devices' information</h2>
          </GridItem>
        </GridContainer>
      </div>
    )
}