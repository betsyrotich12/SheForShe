import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <div className="container">
                <Link className="navbar-brand" to="/">Gender Equity Platform</Link>
                <div className="collapse navbar-collapse">
                    <ul className="navbar-nav ml-auto">
                        <li className="nav-item"><Link className="nav-link" to="/">Home</Link></li>
                        <li className="nav-item"><Link className="nav-link" to="/mentorship">Mentorship</Link></li>
                        <li className="nav-item"><Link className="nav-link" to="/forum">Forum</Link></li>
                        <li className="nav-item"><Link className="nav-link" to="/stories">Stories</Link></li>
                    </ul>
                </div>
            </div>
        </nav>
    );
}

export default Navbar;
