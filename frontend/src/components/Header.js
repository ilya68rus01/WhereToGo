import { Nav, Navbar, Collapse, Form, Button } from "bootstrap-4-react/lib/components";
import React from "react";

class Header extends React.Component {
    render() {
        return(
            <div className="HeaderNav">
                <Navbar expand="lg" dark bg="primary" mb="3">
                    <Navbar.Brand href="#">WhereToGo</Navbar.Brand>
                    <Navbar.Toggler target="#navbarColor2" />
                    <Collapse navbar id="navbarColor2">
                        <Navbar.Nav mr="auto">
                            <Nav.ItemLink href="#" active>Главная</Nav.ItemLink>
                            <Nav.ItemLink href="#">Рекомендации</Nav.ItemLink>
                            <Nav.ItemLink href="#">Избранное</Nav.ItemLink>
                        </Navbar.Nav>
                        <Form inline my="2 lg-0">
                        <Button outline light my="2 sm-0">SignIn</Button>
                        </Form>
                    </Collapse>
                </Navbar>
            </div>
        )
    }
}

export default Header;