import React from "react"
import { Nav, NavLink, NavMenu }
    from "./NavbarElements";

const Navbar = () => {
    return (
        <>
            <Nav>
                <NavMenu>
                    <NavLink to="./" activeStyle>
                        Home
                    </NavLink>
                    <NavLink to="./login" activeStyle>
                        Log in
                    </NavLink>
                    <NavLink to="./signup" activeStyle>
                        Sign Up
                    </NavLink>
                    <NavLink to="./portfolio" activeStyle>
                        Portfolio
                    </NavLink>
                    <NavLink to="./contact" activeStyle>
                        Contact Us
                    </NavLink>
                </NavMenu>
            </Nav>
        </>
    );
};
export default Navbar;