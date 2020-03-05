import React, { useState, useEffect } from 'react';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import Box from '@material-ui/core/Box';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import axios from 'axios';
import { Redirect, useHistory } from 'react-router-dom';

function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {'Copyright © '}
      <Link color="inherit" href="https://material-ui.com/">
        Defensya
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const useStyles = makeStyles(theme => ({
  paper: {
    marginTop: theme.spacing(8),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: '100%', // Fix IE 11 issue.
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));

export default function SignIn() {

  let history = useHistory();

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const classes = useStyles();

  /**
   * Al entrar en la vista, comprobamos si estamos haciendo login o logout
   * En caso de haber pulsado la opcion de logout, borraremos todo el localStorage
   * y podremos volver a logear.
   */
  useEffect(() => {
    if (localStorage.getItem('token')) {
      localStorage.clear();

      axios.post('http://127.0.0.1:8000/rest-auth/logout/', {
      }, )
      .then(function (response) {
        console.log(response);
        window.location.reload();
      })
      .catch(function (error) {
        console.log(error);
      });
    }
  }, []);


  /**
   * Evento que salta al hacer submit del formulario.
   * Envia una peticion al servidor con el login y 
   * recoge el auth token para poder hacer operaciones
   * dentro de nuestra aplicacion.
   */
  const submitForm = () => {
    axios.post('http://127.0.0.1:8000/rest-auth/login/', {
      username: username,
      password: password
    }, )
    .then(function (response) {
      console.log(response);
      localStorage.setItem('username', username);
      localStorage.setItem('token', 'Token: ' + response.data.key);
      history.push('/dashboard');
      window.location.reload();
      
    })
    .catch(function (error) {
      console.log(error);
    });
  }

  /**
   * Al pulsar la tecla enter, haremos submit del form
   * @param {*} event 
   */
  const handleKeyPress = (event) => {
    if(event.key === 'Enter'){
      submitForm();
    }
  }

  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <div className={classes.paper}>
        <Avatar className={classes.avatar}>
          <LockOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          Sign in
        </Typography>
        <form className={classes.form} noValidate>
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="username"
            label="Username"
            name="username"
            autoComplete="username"
            onChange={(e)=>setUsername(e.target.value)}
            onKeyPress={(e) => handleKeyPress(e)}
            autoFocus
          />
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            onChange={(e)=>setPassword(e.target.value)}
            onKeyPress={(e) => handleKeyPress(e)}
            autoComplete="current-password"
          />
          <Button
            type="button"
            fullWidth
            variant="contained"
            color="primary"
            className={classes.submit}
            onClick={() => submitForm()}
          >
            Sign in
          </Button>
        </form>
      </div>
      <Box mt={8}>
        <Copyright />
      </Box>
    </Container>
  );
}