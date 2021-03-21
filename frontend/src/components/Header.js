import React from "react";
import { Button, Collapse, Form, Nav, Navbar, Modal} from "bootstrap-4-react";
import SignInModal from "./SignInModal";

class Header extends React.Component {
    render() {
        return(
            <div className="HeaderNav">
                <Navbar expand="lg" dark  bg="primary" mb="3">
                    <Navbar.Brand href="http://localhost:3000/">WhereToGo</Navbar.Brand>
                    <Navbar.Toggler target="#navbarColor2" />
                    <Collapse navbar id="navbarColor2">
                        <Nav mr="auto">
                            <Nav.ItemLink href="#" active>Главная</Nav.ItemLink>
                            <Nav.ItemLink href="#">Рекомендации</Nav.ItemLink>
                            <Nav.ItemLink href="#">Избранное</Nav.ItemLink>
                        </Nav>
                        <Form inline my="2 lg-0">
                        <Button data-toggle="modal" data-target="#signInModal" outline light my="2 sm-0">SignIn</Button>
                        </Form>
                    </Collapse>
                </Navbar>
                <SignInModal />
            </div>
        )
    }
}

export default Header;