import React, { Component } from 'react';
import TextField from 'material-ui/TextField';
import RaisedButton from 'material-ui/RaisedButton';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import '../css/LoginScreen.css';

class LoginScreen extends Component {

  render() {

    return (

    <div className="container">
      <MuiThemeProvider>
        <TextField
            hintText="Username"
            onChange={this.props.textHandler} 
            underlineFocusStyle={{borderColor: '#440014'}}
        />
        <RaisedButton 
            label="Login"
            style = {{ margin: '15px' }}
        />
      </MuiThemeProvider>
    </div>
    );
  }
}

export default LoginScreen;
