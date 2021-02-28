import React from 'react';
import Place from './Place';
import { Card } from "bootstrap-4-react/lib/components";
import { Container, Row, Col } from 'bootstrap-4-react';

class AllPlaces extends React.Component {
    render() {
        const {places} = this.props
        return(
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
        );
    }
}

export default AllPlaces