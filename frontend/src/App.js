import React, {useEffect, useState} from "react";
import AllPlaces from './components/AllPlaces'
import './App.css';
import Header from "./components/Header";
import { Container, Row } from "bootstrap-4-react/lib/components/layout";

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
        <Container>
          <AllPlaces places={places}></AllPlaces>
        </Container>
    </div>
  );
}

export default App;
