import React, { useState, useEffect }  from 'react'
import GridContainer from "components/Grid/GridContainer";
import GridItem from "components/Grid/GridItem.js";
import Card from "components/Card/Card.js";
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

    const [logs, setLogs] = useState([]);

    var array = []

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/log', { headers: { "Authorization": token } })
          .then(function (response) {
    
            for(var i in response.data) {
                let datos = response.data[i]['data'].split(",");
                let arrayDatos = []
                for(var j in datos) {
                    arrayDatos.push(datos[j])
                }
                console.log(arrayDatos)
                array.push([response.data[i]['timestamp'], datos[1], datos[2], datos[3], datos[4],datos[5], datos[6], datos[7], datos[8], datos[9], datos[10], datos[11]]);
            }
            setLogs(array);
          })
          .catch(function (error) {
            console.log(error)
          });
      }, []);


    return (
        <GridContainer>
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
                    tableHead={["Date", "Temp upper", "Temp lower", "Temp Amb", "Temp Oil", "PressureDie", "PressurePump", "Scale1", "Scale2", "Scale3", "Mode", "Freq"]}
                    tableData={logs}
                    />
                </CardBody>
                </Card>
            </GridItem>
        </GridContainer>
    )
}