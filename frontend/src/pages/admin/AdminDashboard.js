import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { moviesAPI, showtimesAPI, auditoriumsAPI } from '../../services/api';
import {
  FaFilm, FaTheaterMasks, FaClock, FaChair,
  FaHistory, FaRocket, FaHome
} from 'react-icons/fa';
import '../../styles/AdminDashboard.css';

const AdminDashboard = () => {
  const [stats, setStats] = useState({
    totalMovies: 0,
    totalShowtimes: 0,
    totalAuditoriums: 0,
    totalSeats: 0,
  });
  const [recentActivities, setRecentActivities] = useState({
    movies: [],
    showtimes: [],
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchStats();
  }, []);

  const fetchStats = async () => {
    try {
      setLoading(true);
      const [moviesRes, showtimesRes, auditoriumsRes] = await Promise.all([
        moviesAPI.getAll(),
        showtimesAPI.getAll(),
        auditoriumsAPI.getAll(),
      ]);

      // Đảm bảo data luôn là array
      const movies = Array.isArray(moviesRes.data) ? moviesRes.data : moviesRes.data.results || [];
      const showtimes = Array.isArray(showtimesRes.data) ? showtimesRes.data : showtimesRes.data.results || [];
      const auditoriums = Array.isArray(auditoriumsRes.data) ? auditoriumsRes.data : auditoriumsRes.data.results || [];

      // Tính tổng số ghế
      const totalSeats = auditoriums.reduce((sum, aud) => sum + (aud.total_seats || 0), 0);

      setStats({
        totalMovies: movies.length,
        totalShowtimes: showtimes.length,
        totalAuditoriums: auditoriums.length,
        totalSeats: totalSeats,
      });

      // Lấy 3 phim mới nhất
      const recentMovies = [...movies]
        .sort((a, b) => new Date(b.release_date || 0) - new Date(a.release_date || 0))
        .slice(0, 3);

      // Lấy 3 suất chiếu mới nhất
      const recentShowtimes = [...showtimes]
        .sort((a, b) => new Date(b.start_time || 0) - new Date(a.start_time || 0))
        .slice(0, 3);

      setRecentActivities({
        movies: recentMovies,
        showtimes: recentShowtimes,
      });
    } catch (err) {
      console.error('Error fetching stats:', err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="admin-page">
        <div className="loading">Đang tải...</div>
      </div>
    );
  }

  return (
    <div className="admin-dashboard">
      <h2>Dashboard</h2>
      
      <div className="stats-grid">
        <div className="stat-card">
          <div className="stat-icon"><FaFilm /></div>
          <div className="stat-info">
            <h3>Tổng số phim</h3>
            <p className="stat-value">{stats.totalMovies}</p>
          </div>
        </div>

        <div className="stat-card">
          <div className="stat-icon"><FaTheaterMasks /></div>
          <div className="stat-info">
            <h3>Phòng chiếu</h3>
            <p className="stat-value">{stats.totalAuditoriums}</p>
          </div>
        </div>

        <div className="stat-card">
          <div className="stat-icon"><FaClock /></div>
          <div className="stat-info">
            <h3>Suất chiếu</h3>
            <p className="stat-value">{stats.totalShowtimes}</p>
          </div>
        </div>

        <div className="stat-card">
          <div className="stat-icon"><FaChair /></div>
          <div className="stat-info">
            <h3>Tổng số ghế</h3>
            <p className="stat-value">{stats.totalSeats}</p>
          </div>
        </div>
      </div>

      <div className="recent-activities">
        <h3><FaHistory style={{marginRight: 8, color: '#c0392b'}} /> Hoạt động gần đây</h3>
        
        <div className="activities-section">
          <div className="activity-column">
            <h4>Phim mới thêm</h4>
            {recentActivities.movies.length > 0 ? (
              <ul className="activity-list">
                {recentActivities.movies.map((movie) => (
                  <li key={movie.id} className="activity-item">
                    <span className="activity-icon"><FaFilm /></span>
                    <div className="activity-content">
                      <strong>{movie.title}</strong>
                      <small>{movie.genre || 'N/A'}</small>
                    </div>
                  </li>
                ))}
              </ul>
            ) : (
              <p className="no-data">Chưa có phim nào</p>
            )}
          </div>

          <div className="activity-column">
            <h4>Suất chiếu mới thêm</h4>
            {recentActivities.showtimes.length > 0 ? (
              <ul className="activity-list">
                {recentActivities.showtimes.map((showtime) => (
                  <li key={showtime.id} className="activity-item">
                    <span className="activity-icon"><FaClock /></span>
                    <div className="activity-content">
                      <strong>{showtime.movie_title || `Showtime #${showtime.id}`}</strong>
                      <small>
                        {new Date(showtime.show_date).toLocaleDateString('vi-VN')} - {showtime.show_time}
                      </small>
                    </div>
                  </li>
                ))}
              </ul>
            ) : (
              <p className="no-data">Chưa có suất chiếu nào</p>
            )}
          </div>
        </div>
      </div>

      <div className="quick-actions">
        <h3><FaRocket style={{marginRight: 8, color: '#c0392b'}} /> Thao tác nhanh</h3>
        <div className="actions-grid">
          <Link to="/admin/movies" className="action-card">
            <span className="action-icon"><FaFilm /></span>
            <span>Quản lý Phim</span>
          </Link>
          <Link to="/admin/auditoriums" className="action-card">
            <span className="action-icon"><FaTheaterMasks /></span>
            <span>Quản lý Phòng chiếu</span>
          </Link>
          <Link to="/admin/showtimes" className="action-card">
            <span className="action-icon"><FaClock /></span>
            <span>Quản lý Suất chiếu</span>
          </Link>
          <Link to="/" className="action-card">
            <span className="action-icon"><FaHome /></span>
            <span>Về trang chủ</span>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default AdminDashboard;
