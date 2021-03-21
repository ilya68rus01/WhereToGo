import React from "react";
import { Button, Modal,Form} from "bootstrap-4-react";

export default class AddPlaceModal extends React.Component {
    render() {
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
                        <Form.Input type="text" id="placeName" placeholder="Название" />
                    </Form.Group>
                    <Form.Group>
                        <label htmlFor="placeAddress">Адрес</label>
                        <Form.Input type="text" id="placeAddress" placeholder="Адрес" />
                    </Form.Group>
                    <Form.Group>
                        <label htmlFor="placeDescription">Описание</label>
                        <Form.Input type="text" id="placeDescription" placeholder="Описание" />
                    </Form.Group>
                </Form>
              </Modal.Body>
              <Modal.Footer>
                <Button  data-dismiss="modal">Cancel</Button>
                <Button primary>Add</Button>
              </Modal.Footer>
            </Modal.Content>
          </Modal.Dialog>
        </Modal>);
    }
}