import React, { useState } from 'react';
import { Outlet, Link, useNavigate, useLocation } from 'react-router-dom';
import { useAuth } from '../../contexts/AuthContext';
import {
  FaChartBar, FaFilm, FaTag, FaTheaterMasks, FaClock,
  FaHome, FaUser, FaChevronLeft, FaChevronRight, FaVideo
} from 'react-icons/fa';
import '../../styles/AdminLayout.css';

const AdminLayout = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();
  const [sidebarOpen, setSidebarOpen] = useState(true);

  const handleLogout = async () => {
    await logout();
    navigate('/login');
  };

  const menuItems = [
    { path: '/admin', label: 'Dashboard', icon: <FaChartBar /> },
    { path: '/admin/movies', label: 'Quản lý Phim', icon: <FaFilm /> },
    { path: '/admin/genres', label: 'Quản lý Thể loại', icon: <FaTag /> },
    { path: '/admin/auditoriums', label: 'Quản lý Phòng chiếu', icon: <FaTheaterMasks /> },
    { path: '/admin/showtimes', label: 'Quản lý Suất chiếu', icon: <FaClock /> },
  ];

  return (
    <div className="admin-layout">
      <aside className={`sidebar ${sidebarOpen ? 'open' : 'closed'}`}>
        <div className="sidebar-header">
          <h2><FaVideo style={{marginRight: 8, color: '#e74c3c'}} /> Admin Panel</h2>
          <button 
            className="toggle-sidebar"
            onClick={() => setSidebarOpen(!sidebarOpen)}
          >
            {sidebarOpen ? <FaChevronLeft /> : <FaChevronRight />}
          </button>
        </div>

        <nav className="sidebar-nav">
          {menuItems.map((item) => (
            <Link
              key={item.path}
              to={item.path}
              className={`sidebar-link ${
                location.pathname === item.path ? 'active' : ''
              }`}
            >
              <span className="icon">{item.icon}</span>
              {sidebarOpen && <span className="label">{item.label}</span>}
            </Link>
          ))}
        </nav>

        <div className="sidebar-footer">
          <Link to="/" className="sidebar-link">
            <span className="icon"><FaHome /></span>
            {sidebarOpen && <span className="label">Về trang chủ</span>}
          </Link>
        </div>
      </aside>

      <div className="admin-main">
        <header className="admin-header">
          <div className="admin-header-content">
            <h1>Quản trị hệ thống</h1>
            <div className="admin-user-menu">
              <span className="admin-user-name"><FaUser style={{marginRight: 6, fontSize: 13}} /> {user?.username}</span>
              <button onClick={handleLogout} className="btn-logout">
                Đăng xuất
              </button>
            </div>
          </div>
        </header>

        <main className="admin-content">
          <Outlet />
        </main>
      </div>
    </div>
  );
};

export default AdminLayout;
