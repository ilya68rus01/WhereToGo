import { Card } from "bootstrap-4-react";
import React from "react";

class Place extends React.Component {
   
    render() {
        const {place} = this.props
        console.log(place);
        return(
        <div className="Place" key={123}>
            <Card style={{width:'18rem', height:'16rem',margin:'0.5rem'}}>
                <Card.Image src={place.photo_src} top/>
                <Card.Body>
                    <Card.Title>
                        {place.name}
                    </Card.Title>
                    <Card.Text>
                        {place.description}
                    </Card.Text>
                </Card.Body>
                <Card.Footer>
                    Рейтинг: {place.rate}
                </Card.Footer>
            </Card>
        </div>
        );
    }
}

export default Place