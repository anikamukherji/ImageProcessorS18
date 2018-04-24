import React, { Component } from 'react';
import ImageProcessor from './ImageProcessor';
import LoginScreen from './LoginScreen';
import '../css/App.css';

class App extends Component {

  constructor() {
    super()
    this.state = {
      userLoggedIn: true,
      currUser: null,
    }
  }

  handleChange = event => {
    // handler for username textbox
    this.setState({
      currUser: event.target.value
    });
  }

  renderContent = () => {
    if (!this.state.userLoggedIn) {
      console.log("returning login screen")
      return (
        <LoginScreen
          textHandler={this.handleChange}
        />
      )
    } else {
      console.log("returning imageprocessor")
      return (
        <ImageProcessor
          username={this.state.currUser}
        />
      ) 
    }
  }

  render() {
    return (
      <div className="App">
        {this.renderContent()}
      </div>
    );
  }
}

export default App;
