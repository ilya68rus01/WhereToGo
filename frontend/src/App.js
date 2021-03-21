import React, {useEffect, useState} from "react";
import AllPlaces from './components/AllPlaces'
import './App.css';
import Header from "./components/Header";
import { Container, Row, Button } from "react-bootstrap";
import AddPlaceModal from "./components/AddPlaceModal";

function App() {
  const [places, setPlaces] = useState([]);

  useEffect(() => {
    async function fetchMyAPI() {
      let response = await fetch('/places')
      response = await response.json()
      setPlaces(JSON.parse(response))
    }

    fetchMyAPI()
  }, [])

  return (
    <div className="App">
        <Header/>
        <AllPlaces places={places}></AllPlaces>
        <AllPlaces places={places}></AllPlaces>
        <AllPlaces places={places}></AllPlaces>
        <AllPlaces places={places}></AllPlaces>
        <AllPlaces places={places}></AllPlaces>
        <div className="addPlaceBtn" style={{position:'fixed', top:'90%', left:'95%'}}>
          <Button success style={{borderRadius:'20px', fontSize:'1.2em'}} data-toggle="modal" data-target="#addPlaceModal" outline light my="2 sm-0" >+</Button>
        </div>
        <AddPlaceModal />
    </div>
  );
  
}

export default App;
