import React, { Component } from 'react';
import ImageProcessor from './ImageProcessor';
import LoginScreen from './LoginScreen';
import '../css/App.css';

class App extends Component {

  constructor() {
    super()
    this.state = {
      userLoggedIn: false,
      isVisitor: false,
      currUser: null,
      usernameWasTaken: false,
    }
  }

  handleChange = event => {
    // handler for username textbox
    this.setState({
      currUser: event.target.value
    });
  }

  didPressLogin = event => {
    // TO DO 
    // call API to see if user already exists
    // if user exists, login to imageprocesoor
    // else require that user creates new user
    this.setState({
      userLoggedIn: true,
    });
  }

  didPressNewUser = event => {
    // TO DO 
    // call API to see if username already taken
    // if available, login to imageprocesoor
    // else require that user chooses different username
    this.setState({
      userLoggedIn: false,
      usernameWasTaken: true,
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
