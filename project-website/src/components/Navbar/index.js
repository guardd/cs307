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
                    <NavLink to="./portfolioChange" activeStyle>
                        Portfolio
                    </NavLink>
                    <NavLink to="./portfolio" activeStyle>
                        Prediction
                    </NavLink>
                    <NavLink to="./profile" activeStyle>
                        Profile
                    </NavLink>
                    <NavLink to="./contact" activeStyle>
                        Contact Us
                    </NavLink>
                    <NavLink to="./trade" activeStyle>
                        Trade
                    </NavLink>
                    <NavLink to="./friend" activeStyle>
                        Friends
                    </NavLink>
                </NavMenu>
            </Nav>
        </>
    );
};
export default Navbar;
