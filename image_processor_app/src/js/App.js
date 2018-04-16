import React, { Component } from 'react';
import '../css/App.css';
import ImageView from './ImageView';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Image Processor</h1>
        </header>

        <ImageView/>
      </div>
    );
  }
}

export default App;
