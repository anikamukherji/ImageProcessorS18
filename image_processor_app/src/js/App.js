import React, { Component } from 'react';
import ImageProcessor from './ImageProcessor';
import LoginScreen from './LoginScreen';
import axios from 'axios';
import '../css/App.css';

//var hostName = "http://vcm-3576.vm.duke.edu:5000/"
var hostName = "http://127.0.0.1:5000/"

class App extends Component {

  constructor() {
    super()
    this.state = {
      userLoggedIn: false,
      isVisitor: false,
      currUser: null,
      usernameWasTaken: false,
      loggedInWithInvalid: false,
    }
  }

  handleChange = event => {
    // handler for username textbox
    this.setState({
      currUser: event.target.value
    });
  }

  didPressLogin = event => {
    // calls API to see if user already exists
    // if user exists, logs in to imageprocesoor
    // else requires that user creates new user
    var requestURL = hostName + "api/user_exists/" + this.state.currUser
    axios.get(requestURL).then( response => { 
      this.setState({
        userLoggedIn: response.data,
        loggedInWithInvalid: !response.data,
      });
    }); 
  }

  didPressNewUser = event => {
    // calls API to see if username already taken
    // if available, logs in to imageprocesoor
    // else requires that user chooses different username
    var r1URL = hostName + "api/user_exists/" + this.state.currUser
    axios.get(r1URL).then( response => { 
      if (response.data) {
        this.setState({
          userLoggedIn: false,
          usernameWasTaken: true,
        });
      } else {
        var r2URL = hostName + "api/new_user" 
        var dict = {"username": this.state.currUser}
        axios.post(r2URL, dict).then( response => { 
          this.setState({
            userLoggedIn: true,
          });
        });
      }
    }); 
  }

  didLoginAsVisitor = event => {
    this.setState({
      currUser: "Visitor",
      isVisitor: true,
    });
  }

  renderContent = () => {
    if (!this.state.userLoggedIn && !this.state.isVisitor) {
      return (
        <LoginScreen
          textHandler={this.handleChange}
          loginHandler={this.didPressLogin}
          newUserHandler={this.didPressNewUser}
          visitorHandler={this.didLoginAsVisitor}
          showTakenUserLabel={this.state.usernameWasTaken}
          showCreateNewUserLabel={this.state.loggedInWithInvalid}
        />
      )
    } else {
      return (
        <ImageProcessor
          username={this.state.currUser}
          isVisitor={this.state.isVisitor}
        />
      ) 
    }
  }

  render() {
    return (
      <div className="App">

        <header className="App-header">
          <h1 className="App-title">Image Processor</h1>
        </header>

        {this.renderContent()}
      </div>
    );
  }
}

export default App;
