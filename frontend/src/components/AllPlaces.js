import React from 'react';
import Place from './Place';
import { Card } from "bootstrap-4-react";
import { Container } from 'react-bootstrap';

class AllPlaces extends React.Component {
    render() {
        const {places} = this.props
        return(
            <Container>
                <div className="AllPlaces">
                    <React.Fragment>
                        <Card.Deck>
                            {places.map(place =>
                                    <Place place={place}>
                                    </Place>
                                )
                            }
                        </Card.Deck> 
                    </React.Fragment>
                </div>
            </Container>
        );
    }
}

export default AllPlaces