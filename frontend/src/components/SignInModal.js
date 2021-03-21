import React from "react";
import { Button, Modal,Form} from "bootstrap-4-react";

export default class SignInModal extends React.Component {
    render() {
        return(
        <Modal id="signInModal" fade>
          <Modal.Dialog>
            <Modal.Content>
              <Modal.Header closeButton >
                <Modal.Title>Sign In</Modal.Title>
                <Modal.Close>
                  <span aria-hidden="true">&times;</span>
                </Modal.Close>
                </Modal.Header>
                <Modal.Body>
                <Form>
                    <Form.Group>
                        <label htmlFor="exampleInputEmail1">Email address</label>
                        <Form.Input type="email" id="exampleInputEmail1" placeholder="Enter email" />
                    </Form.Group>
                    <Form.Group controlId="formBasicPassword">
                        <label htmlFor="InputPassword1">Password</label>
                        <Form.Input type="password" id="exampleInputPassword1" placeholder="Enter password" />
                    </Form.Group>
                </Form>
              </Modal.Body>
              <Modal.Footer>
                <Button primary data-dismiss="modal">Sign In</Button>
              </Modal.Footer>
            </Modal.Content>
          </Modal.Dialog>
        </Modal>);
    }
}