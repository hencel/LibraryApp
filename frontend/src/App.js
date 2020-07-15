import React from 'react';
import logo from './logo.svg';
import './App.css';

import PersonList from './Components/PersonList';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Hello django</h1>
      </header>	
	  <PersonList />
    </div>
  );
}

export default App;
