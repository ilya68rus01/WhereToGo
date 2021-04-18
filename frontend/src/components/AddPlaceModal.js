import React from "react";
import { Button, Modal,Form} from "bootstrap-4-react";

export default class AddPlaceModal extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      name:'',
      adress:'',
      description:'',
      rate:'',
      img_src: null
    }
  }

  changeHandler = e => {
    this.setState({[e.target.name]: e.target.value})
  }

  addPlace = e => {
    e.preventDefault()
    fetch("/places", {
      method: "post",
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      //make sure to serialize your JSON body
      body: JSON.stringify(this.state)
    })
  }

    render() {
      const {name,adress,description,rate,img_src} = this.state
        return(
        <Modal id="addPlaceModal" fade>
          <Modal.Dialog>
            <Modal.Content>
              <Modal.Header closeButton >
                <Modal.Title>Add Place</Modal.Title>
                <Modal.Close>
                  <span aria-hidden="true">&times;</span>
                </Modal.Close>
                </Modal.Header>
                <Modal.Body>
                <Form>
                    <Form.Group>
                        <label htmlFor="placeName">Назване</label>
                        <Form.Input name='name' type="text" id="placeName" placeholder="Название" value={name} onChange={this.changeHandler}/>
                    </Form.Group>
                    <Form.Group>
                        <label htmlFor="placeAddress">Адрес</label>
                        <Form.Input name='adress' type="text" id="placeAddress" placeholder="Адрес" value={adress} onChange={this.changeHandler}/>
                    </Form.Group>
                    <Form.Group>
                        <label htmlFor="placeDescription">Описание</label>
                        <Form.Input name='description' type="text" id="placeDescription" placeholder="Описание" value={description} onChange={this.changeHandler}/>
                    </Form.Group>
                    <Form.Group>
                        <label htmlFor="placeRate">Оценка</label>
                        <Form.Input name='rate' type="text" id="placeRate" placeholder="Оценка" value={rate}  onChange={this.changeHandler}/>
                    </Form.Group>
                </Form>
              </Modal.Body>
              <Modal.Footer>
                <Button  data-dismiss="modal">Cancel</Button>
                <Button onClick={this.addPlace} primary>Add</Button>
              </Modal.Footer>
            </Modal.Content>
          </Modal.Dialog>
        </Modal>);
    }
}