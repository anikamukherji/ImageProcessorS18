import React, { Component } from 'react';
import TextField from 'material-ui/TextField';
import RaisedButton from 'material-ui/RaisedButton';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import '../css/LoginScreen.css';

class LoginScreen extends Component {

  renderWarning = () => {
    if (this.props.showTakenUserLabel) {
      return (
        <p className="warning-label">Username is Taken: Please Choose Another </p>
      )
    } else if (this.props.showCreateNewUserLabel) {
      return (
        <p className="warning-label">Username Does Not Exist: Please Create New User</p>
      )
    }
  }

  render() {
    return (

    <div className="container">
      <MuiThemeProvider>
        <div className="content">
          <TextField
              hintText="Username"
              onChange={this.props.textHandler} 
              underlineFocusStyle={{borderColor: '#440014'}}
          />

          {this.renderWarning()}

          <div className="buttons">
            <RaisedButton 
                label="Login as New User"
                style= {{ margin: '15px' }}
                onClick= {this.props.newUserHandler}
            />
            <RaisedButton 
                label="Login as Existing User"
                style= {{ margin: '15px' }}
                onClick= {this.props.loginHandler}
            />
            <RaisedButton 
                label="Login as Visitor"
                style= {{ margin: '15px' }}
                onClick= {this.props.visitorHandler}
            />
          </div>

          <div align="center" className="footer">
            <p> BME590 Final Project </p>
            <p> Anika Mukherji </p>
            <p> Zhiwei Kang </p>
            <p> Yi Zhao </p>
          </div>

        </div>
      </MuiThemeProvider>
    </div>
    );
  }
}

export default LoginScreen;
