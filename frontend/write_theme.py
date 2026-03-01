"""Overwrite all CSS files with dark red cinema theme."""
import os

BASE = r"C:\Users\Admin\BTL-CSDL-PTIT\frontend\src\styles"

files = {}

# ─────────────────────────────────────────────
files["App.css"] = """\
.App { min-height: 100vh; display: flex; flex-direction: column; }

.loading-screen {
  display: flex; justify-content: center; align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #0d0d0d 0%, #1a0000 100%);
  color: #f0f0f0; font-size: 1.5rem;
}

.loading-spinner { animation: pulse 1.5s ease-in-out infinite; }

@keyframes pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50%       { opacity: 0.5; transform: scale(1.1); }
}
"""

# ─────────────────────────────────────────────
files["Layout.css"] = """\
.layout { min-height: 100vh; display: flex; flex-direction: column; }

/* Header */
.header {
  background: linear-gradient(135deg, #111111 0%, #1a0000 100%);
  color: #f0f0f0; padding: 0;
  box-shadow: 0 2px 12px rgba(192,57,43,0.2);
  position: sticky; top: 0; z-index: 100;
  border-bottom: 1px solid rgba(192,57,43,0.25);
}
.header-content { display: flex; justify-content: space-between; align-items: center; padding: 16px 0; }
.logo { font-size: 24px; font-weight: bold; color: #f0f0f0; text-decoration: none; display: flex; align-items: center; gap: 8px; }
.logo span { color: #e74c3c; }

.nav { display: flex; gap: 24px; align-items: center; }
.nav-link {
  color: #dddddd; text-decoration: none; font-weight: 500;
  transition: all 0.3s; padding: 8px 12px; border-radius: 6px;
}
.nav-link:hover { background: rgba(192,57,43,0.15); color: #e74c3c; }
.nav-link.admin-link {
  background: linear-gradient(135deg, rgba(192,57,43,0.25), rgba(139,0,0,0.2));
  border: 1px solid rgba(192,57,43,0.4); padding: 10px 20px; font-weight: 600;
  box-shadow: 0 2px 8px rgba(192,57,43,0.15); backdrop-filter: blur(10px);
  transition: all 0.3s cubic-bezier(0.4,0,0.2,1);
}
.nav-link.admin-link:hover {
  background: linear-gradient(135deg, rgba(231,76,60,0.35), rgba(192,57,43,0.25));
  transform: translateY(-2px); box-shadow: 0 4px 12px rgba(192,57,43,0.3);
  border-color: rgba(231,76,60,0.6); color: #fff;
}

/* Auth buttons */
.auth-section { display: flex; align-items: center; gap: 12px; }
.user-menu { display: flex; align-items: center; gap: 16px; }
.user-name { font-weight: 500; color: #dddddd; }

.btn-logout {
  background: linear-gradient(135deg, rgba(192,57,43,0.25), rgba(139,0,0,0.2));
  color: #f0f0f0; border: 1px solid rgba(192,57,43,0.4); padding: 10px 20px;
  border-radius: 8px; cursor: pointer; font-weight: 600;
  box-shadow: 0 2px 8px rgba(192,57,43,0.15); backdrop-filter: blur(10px);
  transition: all 0.3s cubic-bezier(0.4,0,0.2,1);
}
.btn-logout:hover {
  background: linear-gradient(135deg, rgba(231,76,60,0.35), rgba(192,57,43,0.25));
  transform: translateY(-2px); box-shadow: 0 4px 12px rgba(192,57,43,0.3);
}

.auth-buttons { display: flex; gap: 12px; }
.btn-login, .btn-register {
  padding: 10px 24px; border-radius: 8px; text-decoration: none;
  font-weight: 600; transition: all 0.3s cubic-bezier(0.4,0,0.2,1);
}
.btn-login {
  color: #f0f0f0;
  background: linear-gradient(135deg, rgba(192,57,43,0.25), rgba(139,0,0,0.2));
  border: 1px solid rgba(192,57,43,0.4); box-shadow: 0 2px 8px rgba(0,0,0,0.2);
}
.btn-register {
  background: linear-gradient(135deg, #c0392b, #8b0000);
  color: #f0f0f0; border: 1px solid rgba(192,57,43,0.5);
  box-shadow: 0 2px 8px rgba(192,57,43,0.3);
}
.btn-login:hover {
  background: linear-gradient(135deg, rgba(231,76,60,0.35), rgba(192,57,43,0.25));
  transform: translateY(-2px); box-shadow: 0 4px 12px rgba(192,57,43,0.3);
}
.btn-register:hover {
  background: linear-gradient(135deg, #e74c3c, #c0392b);
  transform: translateY(-2px); box-shadow: 0 4px 16px rgba(192,57,43,0.4);
}

/* Main Content */
.main-content { flex: 1; padding: 40px 0; background: #0d0d0d; }

/* Footer */
.footer {
  background: #111111; color: #aaaaaa; padding: 24px 0;
  text-align: center; margin-top: auto;
  border-top: 1px solid rgba(192,57,43,0.2);
}

@media (max-width: 768px) {
  .header-content { flex-direction: column; gap: 16px; }
  .nav { flex-direction: column; gap: 8px; }
}
"""

# ─────────────────────────────────────────────
files["Auth.css"] = """\
.auth-page {
  min-height: 100vh; display: flex; align-items: center; justify-content: center;
  background: radial-gradient(ellipse at top, #1a0000 0%, #0d0d0d 60%);
  padding: 20px;
}
.auth-container { width: 100%; max-width: 480px; }
.auth-box {
  background: #1a1a1a; border-radius: 12px; padding: 40px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.6), 0 0 0 1px rgba(192,57,43,0.2);
}
.auth-box.register-box { max-width: 600px; margin: 0 auto; }
.auth-title { font-size: 32px; font-weight: bold; color: #f0f0f0; margin-bottom: 8px; text-align: center; }
.auth-subtitle { color: #aaaaaa; text-align: center; margin-bottom: 32px; }
.auth-form { display: flex; flex-direction: column; gap: 20px; }
.form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.form-group { display: flex; flex-direction: column; gap: 8px; }
.form-group label { font-weight: 600; color: #dddddd; font-size: 14px; }
.form-group input, .form-group select {
  padding: 12px 16px; border: 2px solid #2a2a2a; border-radius: 8px;
  font-size: 14px; transition: all 0.3s; background: #111111; color: #f0f0f0;
}
.form-group input:focus, .form-group select:focus {
  outline: none; border-color: #c0392b; box-shadow: 0 0 0 3px rgba(192,57,43,0.15);
}
.form-group input::placeholder { color: #555555; }
.field-error { color: #e74c3c; font-size: 12px; margin-top: 4px; }
.error-message {
  background: rgba(192,57,43,0.12); color: #e74c3c;
  padding: 12px 16px; border-radius: 8px; font-size: 14px;
  border-left: 4px solid #c0392b;
}
.btn-submit {
  background: linear-gradient(135deg, #c0392b 0%, #8b0000 100%);
  color: #f0f0f0; border: none; padding: 14px; border-radius: 8px;
  font-size: 16px; font-weight: 600; cursor: pointer; transition: all 0.3s; margin-top: 8px;
}
.btn-submit:hover:not(:disabled) { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(192,57,43,0.4); background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%); }
.btn-submit:disabled { opacity: 0.5; cursor: not-allowed; }
.auth-footer { text-align: center; margin-top: 24px; color: #aaaaaa; }
.auth-link { color: #e74c3c; text-decoration: none; font-weight: 600; }
.auth-link:hover { text-decoration: underline; color: #ff6b6b; }

@media (max-width: 640px) { .form-row { grid-template-columns: 1fr; } .auth-box { padding: 24px; } }
"""

# ─────────────────────────────────────────────
files["HomePage.css"] = """\
.home-page { padding-bottom: 40px; background: #0d0d0d; }

/* Hero */
.hero-section {
  background: radial-gradient(ellipse at top, #2d0000 0%, #111111 55%);
  color: #f0f0f0; padding: 80px 0; margin-bottom: 40px;
  position: relative; overflow: hidden;
  border-bottom: 1px solid rgba(192,57,43,0.25);
}
.hero-section::before {
  content: ''; position: absolute; inset: 0;
  background: url('data:image/svg+xml,<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg"><defs><pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M 40 0 L 0 0 0 40" fill="none" stroke="%23c0392b" stroke-width="0.4" opacity="0.15"/></pattern></defs><rect width="100%25" height="100%25" fill="url(%23grid)"/></svg>');
  opacity: 0.5;
}
.hero-title { font-size: 52px; font-weight: 800; margin-bottom: 16px; text-align: center; text-shadow: 0 2px 20px rgba(192,57,43,0.4); position: relative; z-index: 1; }
.hero-subtitle { font-size: 22px; text-align: center; margin-bottom: 40px; opacity: 0.85; position: relative; z-index: 1; font-weight: 400; color: #cccccc; }

.search-form { max-width: 700px; margin: 0 auto; display: flex; gap: 12px; position: relative; z-index: 1; }
.search-input {
  flex: 1; padding: 16px 24px; border: 2px solid rgba(192,57,43,0.3);
  border-radius: 12px; font-size: 16px; background: rgba(17,17,17,0.95);
  color: #f0f0f0; transition: all 0.3s; backdrop-filter: blur(10px);
}
.search-input:focus { outline: none; border-color: #e74c3c; background: #111; box-shadow: 0 4px 16px rgba(192,57,43,0.2); }
.search-input::placeholder { color: #555; }
.search-button {
  padding: 14px 32px; background: linear-gradient(135deg, #c0392b 0%, #8b0000 100%);
  color: #f0f0f0; border: 2px solid rgba(192,57,43,0.3); border-radius: 12px;
  font-size: 16px; font-weight: 700; cursor: pointer; transition: all 0.3s;
  display: flex; align-items: center; gap: 8px;
}
.search-button:hover { background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%); transform: translateY(-2px); box-shadow: 0 8px 24px rgba(192,57,43,0.35); }

/* Section Header */
.section-header { margin-bottom: 32px; text-align: center; }
.section-header h2 { font-size: 36px; font-weight: 800; color: #f0f0f0; position: relative; display: inline-block; padding-bottom: 12px; }
.section-header h2::after {
  content: ''; position: absolute; bottom: 0; left: 50%; transform: translateX(-50%);
  width: 60px; height: 4px; background: linear-gradient(90deg, #c0392b, #8b0000); border-radius: 2px;
}

/* Movies Grid */
.movies-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 24px; }
.movie-card {
  background: #1a1a1a; border-radius: 16px; overflow: hidden;
  box-shadow: 0 4px 16px rgba(0,0,0,0.4); transition: all 0.4s cubic-bezier(0.4,0,0.2,1);
  cursor: pointer; border: 1px solid #2a2a2a;
}
.movie-card:hover { transform: translateY(-8px); box-shadow: 0 12px 32px rgba(192,57,43,0.25); border-color: rgba(192,57,43,0.4); }

.movie-poster { width: 100%; height: 380px; overflow: hidden; background: #111; }
.movie-poster img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s; }
.movie-card:hover .movie-poster img { transform: scale(1.04); }
.poster-placeholder { width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-size: 80px; background: linear-gradient(135deg, #1a0000 0%, #2d0000 100%); }

.movie-info { padding: 20px; }
.movie-title { font-size: 18px; font-weight: bold; margin-bottom: 10px; color: #f0f0f0; }
.movie-meta { display: flex; gap: 12px; margin-bottom: 12px; flex-wrap: wrap; }
.movie-rating, .movie-duration { font-size: 13px; color: #aaaaaa; display: flex; align-items: center; gap: 4px; }
.movie-genres { display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 12px; }
.genre-tag { padding: 3px 10px; background: rgba(192,57,43,0.15); color: #e74c3c; border-radius: 12px; font-size: 12px; font-weight: 500; border: 1px solid rgba(192,57,43,0.25); }

.btn-book-now {
  width: 100%; padding: 10px; background: linear-gradient(135deg, #c0392b 0%, #8b0000 100%);
  color: #f0f0f0; border: none; border-radius: 8px; font-weight: 600;
  cursor: pointer; transition: all 0.3s; font-size: 14px;
}
.btn-book-now:hover { background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%); box-shadow: 0 4px 12px rgba(192,57,43,0.35); }

.no-movies { text-align: center; padding: 60px; color: #aaaaaa; }
.movies-section { padding: 0 0 40px; }
"""

# ─────────────────────────────────────────────
files["AdminLayout.css"] = """\
.admin-layout { display: flex; min-height: 100vh; background: #0d0d0d; }

/* Sidebar */
.sidebar {
  width: 250px; background: #111111; color: #f0f0f0;
  transition: width 0.3s; position: sticky; top: 0; height: 100vh; overflow-y: auto;
  border-right: 1px solid rgba(192,57,43,0.2);
}
.sidebar.closed { width: 80px; }
.sidebar-header {
  padding: 24px; display: flex; justify-content: space-between; align-items: center;
  border-bottom: 1px solid rgba(192,57,43,0.2);
}
.sidebar-header h2 { font-size: 20px; white-space: nowrap; color: #f0f0f0; }
.sidebar.closed .sidebar-header h2 { display: none; }

.toggle-sidebar {
  background: rgba(192,57,43,0.15); border: 1px solid rgba(192,57,43,0.3);
  color: #f0f0f0; width: 32px; height: 32px; border-radius: 6px;
  cursor: pointer; font-size: 16px; transition: all 0.3s;
}
.toggle-sidebar:hover { background: rgba(192,57,43,0.3); }

.sidebar-nav { padding: 16px 0; }
.sidebar-link {
  display: flex; align-items: center; gap: 16px; padding: 14px 24px;
  color: #aaaaaa; text-decoration: none; transition: all 0.3s; font-weight: 500;
}
.sidebar-link:hover { background: rgba(192,57,43,0.1); color: #f0f0f0; }
.sidebar-link.active {
  background: rgba(192,57,43,0.18); color: #e74c3c;
  border-left: 4px solid #c0392b;
}
.sidebar-link .icon { font-size: 22px; width: 32px; text-align: center; }
.sidebar.closed .sidebar-link .label { display: none; }
.sidebar-footer { margin-top: auto; padding: 16px 0; border-top: 1px solid rgba(192,57,43,0.15); }

/* Admin Main */
.admin-main { flex: 1; display: flex; flex-direction: column; overflow-x: hidden; }
.admin-header {
  background: #161616; box-shadow: 0 2px 8px rgba(0,0,0,0.4);
  padding: 0 32px; position: sticky; top: 0; z-index: 10;
  border-bottom: 1px solid rgba(192,57,43,0.15);
}
.admin-header-content { display: flex; justify-content: space-between; align-items: center; padding: 20px 0; }
.admin-header h1 { font-size: 24px; color: #f0f0f0; }
.admin-user-menu { display: flex; align-items: center; gap: 16px; }
.admin-user-name { font-weight: 500; color: #aaaaaa; }
.admin-content { flex: 1; padding: 32px; background: #0d0d0d; }

@media (max-width: 768px) {
  .sidebar { position: fixed; z-index: 100; transform: translateX(-100%); }
  .sidebar.open { transform: translateX(0); }
  .admin-main { width: 100%; }
}
"""

# ─────────────────────────────────────────────
files["AdminDashboard.css"] = """\
.admin-dashboard { min-height: 500px; }
.admin-dashboard h2 { margin-bottom: 30px; color: #f0f0f0; font-size: 32px; }

.stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 40px; }
.stat-card {
  background: linear-gradient(135deg, #1a1a1a 0%, #2d0000 100%);
  padding: 25px; border-radius: 12px; display: flex; align-items: center; gap: 20px;
  color: #f0f0f0; box-shadow: 0 4px 15px rgba(0,0,0,0.3);
  border: 1px solid rgba(192,57,43,0.2);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.stat-card:hover { transform: translateY(-5px); box-shadow: 0 6px 25px rgba(192,57,43,0.25); }
.stat-card:nth-child(2) { background: linear-gradient(135deg, #1a1a1a 0%, #1a0020 100%); }
.stat-card:nth-child(3) { background: linear-gradient(135deg, #1a1a1a 0%, #001a2a 100%); }
.stat-card:nth-child(4) { background: linear-gradient(135deg, #1a1a1a 0%, #001a10 100%); }
.stat-icon { font-size: 48px; }
.stat-info h3 { margin: 0 0 8px 0; font-size: 16px; font-weight: 500; opacity: 0.8; }
.stat-value { font-size: 32px; font-weight: 700; margin: 0; }

.recent-activities {
  background: #1a1a1a; padding: 30px; border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.3); border: 1px solid #2a2a2a;
}
.recent-activities h3 {
  margin: 0 0 25px 0; color: #f0f0f0; font-size: 24px;
  padding-bottom: 15px; border-bottom: 2px solid #2a2a2a;
}
.activities-section { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
.activity-column h4 { margin: 0 0 15px 0; color: #e74c3c; font-size: 18px; }
.activity-list { list-style: none; padding: 0; margin: 0; }
.activity-item {
  display: flex; align-items: flex-start; gap: 12px; padding: 15px;
  border-radius: 8px; background: #111111; margin-bottom: 12px;
  transition: all 0.3s; border-left: 3px solid transparent; border: 1px solid #2a2a2a;
}
.activity-item:hover { background: #1f1f1f; border-left-color: #c0392b; transform: translateX(4px); }
.activity-icon { font-size: 22px; flex-shrink: 0; }
.activity-content { display: flex; flex-direction: column; gap: 4px; flex: 1; }
.activity-content strong { color: #f0f0f0; font-size: 15px; }
.activity-content small { color: #888888; font-size: 13px; }
.no-data { color: #666; font-style: italic; text-align: center; padding: 20px; }
.loading { text-align: center; padding: 40px; font-size: 18px; color: #888; }
"""

# ─────────────────────────────────────────────
files["AdminPages.css"] = """\
/* Admin Pages Common */
.admin-dashboard h2 { font-size: 28px; margin-bottom: 24px; color: #f0f0f0; }

.stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 24px; margin-bottom: 40px; }
.stat-card {
  background: #1a1a1a; padding: 24px; border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.3); display: flex; align-items: center; gap: 20px;
  transition: all 0.3s; border: 1px solid #2a2a2a;
}
.stat-card:hover { transform: translateY(-4px); box-shadow: 0 4px 16px rgba(192,57,43,0.2); }
.stat-icon {
  font-size: 48px; width: 70px; height: 70px; display: flex; align-items: center; justify-content: center;
  background: linear-gradient(135deg, #c0392b 0%, #8b0000 100%); border-radius: 12px;
}
.stat-info h3 { font-size: 14px; color: #aaaaaa; margin-bottom: 8px; }
.stat-value { font-size: 32px; font-weight: bold; color: #f0f0f0; }

.quick-actions { background: #1a1a1a; padding: 32px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.3); border: 1px solid #2a2a2a; }
.quick-actions h3 { font-size: 20px; margin-bottom: 20px; color: #f0f0f0; }
.actions-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; }
.action-card {
  display: flex; flex-direction: column; align-items: center; gap: 12px; padding: 24px;
  background: #111111; border: 2px solid #2a2a2a; border-radius: 12px;
  text-decoration: none; color: #dddddd; font-weight: 600; transition: all 0.3s;
}
.action-card:hover { border-color: #c0392b; background: #1a1a1a; transform: translateY(-4px); box-shadow: 0 4px 12px rgba(192,57,43,0.2); color: #e74c3c; }
.action-icon { font-size: 36px; }

.admin-page { background: #1a1a1a; padding: 32px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.3); border: 1px solid #2a2a2a; }
.page-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; }
.page-header h2 { font-size: 28px; color: #f0f0f0; }

.btn-primary {
  padding: 12px 24px; background: linear-gradient(135deg, #c0392b 0%, #8b0000 100%);
  color: #f0f0f0; border: none; border-radius: 8px; font-weight: 600; cursor: pointer; transition: all 0.3s;
}
.btn-primary:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(192,57,43,0.4); background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%); }
.btn-secondary {
  padding: 12px 24px; background: #111111; color: #aaaaaa; border: 2px solid #333333;
  border-radius: 8px; font-weight: 600; cursor: pointer; transition: all 0.3s;
}
.btn-secondary:hover { border-color: #555; background: #1a1a1a; color: #f0f0f0; }

/* Modal */
.modal-overlay {
  position: fixed; inset: 0; background: rgba(0,0,0,0.8);
  display: flex; align-items: center; justify-content: center; z-index: 1000; padding: 20px;
}
.modal-content {
  background: #1a1a1a; border-radius: 12px; max-width: 600px; width: 100%;
  max-height: 90vh; overflow-y: auto; box-shadow: 0 20px 60px rgba(0,0,0,0.7);
  border: 1px solid rgba(192,57,43,0.25);
}
.modal-header {
  display: flex; justify-content: space-between; align-items: center;
  padding: 24px; border-bottom: 1px solid #2a2a2a;
}
.modal-header h3 { font-size: 20px; color: #f0f0f0; }
.btn-close {
  background: none; border: none; font-size: 24px; color: #666; cursor: pointer;
  width: 32px; height: 32px; display: flex; align-items: center; justify-content: center;
  border-radius: 6px; transition: all 0.3s;
}
.btn-close:hover { background: #2a2a2a; color: #f0f0f0; }

/* Admin Form */
.admin-form { padding: 24px; }
.admin-form .form-group { margin-bottom: 20px; }
.admin-form label { display: block; font-weight: 600; color: #dddddd; margin-bottom: 8px; font-size: 14px; }
.admin-form input, .admin-form select, .admin-form textarea {
  width: 100%; padding: 12px 16px; border: 2px solid #2a2a2a; border-radius: 8px;
  font-size: 14px; transition: all 0.3s; background: #111111; color: #f0f0f0;
}
.admin-form input:focus, .admin-form select:focus, .admin-form textarea:focus {
  outline: none; border-color: #c0392b; box-shadow: 0 0 0 3px rgba(192,57,43,0.12);
}
.admin-form input::placeholder, .admin-form textarea::placeholder { color: #555; }
.form-row { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; }
.form-note { background: rgba(192,57,43,0.08); padding: 12px; border-radius: 6px; margin-bottom: 20px; font-size: 13px; color: #aaaaaa; line-height: 1.6; border-left: 3px solid rgba(192,57,43,0.3); }
.form-actions { display: flex; gap: 12px; justify-content: flex-end; padding-top: 20px; border-top: 1px solid #2a2a2a; }

/* Data Table */
.data-table { overflow-x: auto; margin-top: 24px; }
.data-table table { width: 100%; border-collapse: collapse; }
.data-table thead { background: #111111; }
.data-table th { padding: 14px 16px; text-align: left; font-weight: 600; color: #aaaaaa; font-size: 14px; border-bottom: 2px solid #2a2a2a; }
.data-table td { padding: 14px 16px; border-bottom: 1px solid #222222; color: #dddddd; }
.data-table tbody tr { transition: all 0.2s; }
.data-table tbody tr:hover { background: #1f1f1f; }

/* Badges */
.badge { padding: 4px 10px; border-radius: 6px; font-size: 12px; font-weight: 600; }
.badge-active   { background: rgba(39,174,96,0.15);  color: #27ae60; }
.badge-inactive { background: rgba(192,57,43,0.15);  color: #e74c3c; }
.badge-pending  { background: rgba(243,156,18,0.15); color: #f39c12; }
.badge-paid     { background: rgba(39,174,96,0.15);  color: #27ae60; }
.badge-canceled { background: rgba(192,57,43,0.15);  color: #e74c3c; }

.btn-edit   { padding: 6px 14px; background: rgba(52,152,219,0.15); color: #3498db; border: 1px solid rgba(52,152,219,0.3); border-radius: 6px; cursor: pointer; transition: all 0.2s; font-weight: 600; font-size: 13px; }
.btn-delete { padding: 6px 14px; background: rgba(192,57,43,0.15); color: #e74c3c; border: 1px solid rgba(192,57,43,0.3); border-radius: 6px; cursor: pointer; transition: all 0.2s; font-weight: 600; font-size: 13px; }
.btn-edit:hover   { background: rgba(52,152,219,0.25); transform: translateY(-1px); }
.btn-delete:hover { background: rgba(192,57,43,0.25); transform: translateY(-1px); }

.search-bar { display: flex; gap: 12px; margin-bottom: 24px; }
.search-bar input {
  flex: 1; padding: 12px 16px; border: 2px solid #2a2a2a; border-radius: 8px;
  font-size: 14px; background: #111111; color: #f0f0f0;
}
.search-bar input:focus { outline: none; border-color: #c0392b; }
.search-bar input::placeholder { color: #555; }

.table-actions { display: flex; gap: 8px; }

.error { background: rgba(192,57,43,0.12); color: #e74c3c; padding: 16px; border-radius: 8px; border-left: 4px solid #c0392b; }
"""

# ─────────────────────────────────────────────
files["MovieDetail.css"] = """\
.movie-detail-page { padding-bottom: 40px; background: #0d0d0d; }

.movie-hero {
  background: radial-gradient(ellipse at top, #2d0000 0%, #0d0d0d 70%);
  color: #f0f0f0; padding: 60px 0; margin-bottom: 40px;
  border-bottom: 1px solid rgba(192,57,43,0.2);
}
.movie-hero-content { display: grid; grid-template-columns: 300px 1fr; gap: 40px; align-items: start; }
.movie-poster-large { width: 300px; height: 450px; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 40px rgba(0,0,0,0.6), 0 0 0 1px rgba(192,57,43,0.2); }
.movie-poster-large img { width: 100%; height: 100%; object-fit: cover; }
.poster-placeholder-large { width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-size: 100px; background: rgba(192,57,43,0.1); }
.movie-details { padding-top: 20px; }
.movie-title { font-size: 42px; font-weight: bold; margin-bottom: 24px; color: #f0f0f0; }
.movie-meta-detail { display: flex; flex-direction: column; gap: 12px; margin-bottom: 24px; }
.meta-item { display: flex; gap: 12px; align-items: center; }
.meta-label { font-weight: 600; color: #aaaaaa; }
.meta-value { color: #dddddd; }
.rating-badge { background: rgba(192,57,43,0.2); padding: 4px 12px; border-radius: 6px; font-weight: bold; color: #e74c3c; border: 1px solid rgba(192,57,43,0.3); }
.movie-description-detail h3 { font-size: 20px; margin-bottom: 12px; color: #f0f0f0; }
.movie-description-detail p { line-height: 1.8; color: #bbbbbb; }

.showtimes-section { background: #1a1a1a; padding: 32px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.4); border: 1px solid #2a2a2a; }
.section-title { font-size: 28px; margin-bottom: 24px; color: #f0f0f0; }
.date-selector { display: flex; gap: 12px; margin-bottom: 24px; flex-wrap: wrap; }
.date-button {
  padding: 12px 24px; border: 2px solid #2a2a2a; background: #111111;
  border-radius: 8px; cursor: pointer; font-weight: 600; transition: all 0.3s; color: #aaaaaa;
}
.date-button:hover { border-color: #c0392b; color: #e74c3c; }
.date-button.active { background: linear-gradient(135deg, #c0392b 0%, #8b0000 100%); color: #f0f0f0; border-color: transparent; }
.showtimes-list { display: flex; flex-direction: column; gap: 12px; }
.showtime-card { display: flex; justify-content: space-between; align-items: center; padding: 16px 20px; border: 2px solid #2a2a2a; background: #111111; border-radius: 8px; transition: all 0.3s; }
.showtime-card:hover { border-color: #c0392b; box-shadow: 0 4px 12px rgba(192,57,43,0.15); }
.showtime-info { display: flex; gap: 24px; align-items: center; }
.showtime-time { font-size: 20px; font-weight: bold; color: #e74c3c; }
.showtime-auditorium { color: #aaaaaa; }
.showtime-price { font-weight: 600; color: #f0f0f0; }
.btn-select-showtime {
  padding: 10px 24px; background: linear-gradient(135deg, #c0392b 0%, #8b0000 100%);
  color: #f0f0f0; border: none; border-radius: 6px; font-weight: 600; cursor: pointer; transition: all 0.3s;
}
.btn-select-showtime:hover { transform: translateY(-2px); box-shadow: 0 6px 16px rgba(192,57,43,0.4); background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%); }
.no-showtimes { text-align: center; padding: 40px; color: #666666; }

@media (max-width: 768px) {
  .movie-hero-content { grid-template-columns: 1fr; }
  .movie-poster-large { width: 100%; height: 300px; }
  .movie-title { font-size: 28px; }
}
"""

# ─────────────────────────────────────────────
files["Booking.css"] = """\
.booking-page { padding: 40px 0; background: #0d0d0d; }

.booking-header { background: #1a1a1a; padding: 24px; border-radius: 12px; margin-bottom: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.4); border: 1px solid #2a2a2a; }
.booking-header h1 { font-size: 32px; margin-bottom: 16px; color: #f0f0f0; }
.showtime-info-booking h2 { font-size: 24px; color: #e74c3c; margin-bottom: 8px; }
.showtime-info-booking p { color: #aaaaaa; font-size: 16px; }

.booking-content { display: grid; grid-template-columns: 1fr 380px; gap: 24px; align-items: start; }

.seats-section { background: #1a1a1a; padding: 32px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.4); border: 1px solid #2a2a2a; }

.screen {
  background: linear-gradient(180deg, #1a0000 0%, #2d0000 100%);
  height: 40px; border-radius: 50% 50% 0 0; margin-bottom: 32px;
  position: relative; display: flex; align-items: center; justify-content: center;
  border: 1px solid rgba(192,57,43,0.3);
}
.screen-label { text-align: center; color: #e74c3c; font-size: 14px; font-weight: 600; letter-spacing: 2px; }

.seats-container { display: flex; flex-direction: column; gap: 12px; margin-bottom: 24px; }
.seat-row { display: flex; gap: 12px; align-items: center; }
.row-label { width: 30px; text-align: center; font-weight: bold; color: #666666; }
.row-seats { display: flex; gap: 8px; flex: 1; justify-content: center; }

.seat {
  width: 36px; height: 36px; border: 2px solid #333333; border-radius: 6px;
  background: #111111; cursor: pointer; transition: all 0.2s; font-size: 12px;
  display: flex; align-items: center; justify-content: center; font-weight: 700; color: #f0f0f0 !important;
}
.seat:hover:not(:disabled) { transform: scale(1.1); border-color: #c0392b; }

.seat-standard, .seat.seat-standard { border-color: #27ae60; background: #0d1a0d; color: #aee6b0 !important; }
.seat-vip, .seat.seat-vip { border-color: #e67e22; background: #1a0e00; color: #f5c697 !important; }
.seat-couple, .seat.seat-couple { border-color: #8e44ad; width: 76px; background: #160a1a; color: #d7aef5 !important; }
.seat-selected, .seat.seat-selected { background: linear-gradient(135deg, #c0392b 0%, #8b0000 100%) !important; color: #ffffff !important; border-color: #c0392b !important; }
.seat-booked, .seat.seat-booked { background: #1f1f1f !important; border-color: #333333 !important; cursor: not-allowed !important; color: #444444 !important; }

.seat-legend { display: flex; gap: 20px; justify-content: center; padding-top: 20px; border-top: 1px solid #2a2a2a; flex-wrap: wrap; }
.legend-item { display: flex; align-items: center; gap: 8px; font-size: 14px; color: #aaaaaa; }
.legend-item .seat { width: 24px; height: 24px; font-size: 10px; }

.booking-summary { background: #1a1a1a; padding: 24px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.4); position: sticky; top: 100px; border: 1px solid #2a2a2a; }
.booking-summary h3 { font-size: 20px; margin-bottom: 20px; color: #f0f0f0; }
.selected-seats-list h4 { font-size: 16px; margin-bottom: 12px; color: #aaaaaa; }
.no-selection { text-align: center; color: #666666; padding: 20px; font-style: italic; }

.seats-list { display: flex; flex-direction: column; gap: 8px; margin-bottom: 20px; max-height: 200px; overflow-y: auto; }
.selected-seat-item { display: flex; justify-content: space-between; align-items: center; padding: 10px 12px; background: #111111; border-radius: 6px; border: 1px solid #2a2a2a; }
.seat-label { font-weight: bold; color: #e74c3c; }
.seat-type-label { color: #666666; font-size: 13px; }
.seat-price { font-weight: 600; color: #f0f0f0; }

.price-summary { border-top: 2px solid #2a2a2a; padding-top: 16px; margin-bottom: 20px; }
.price-row { display: flex; justify-content: space-between; align-items: center; color: #aaaaaa; }
.total-price { font-size: 24px; font-weight: bold; color: #e74c3c; }

.btn-continue {
  width: 100%; padding: 14px; background: linear-gradient(135deg, #c0392b 0%, #8b0000 100%);
  color: #f0f0f0; border: none; border-radius: 8px; font-size: 16px; font-weight: 600; cursor: pointer; transition: all 0.3s;
}
.btn-continue:hover:not(:disabled) { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(192,57,43,0.4); background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%); }
.btn-continue:disabled { opacity: 0.4; cursor: not-allowed; }

.booking-note { margin-top: 16px; padding: 12px; background: rgba(192,57,43,0.08); border-radius: 6px; font-size: 13px; color: #aaaaaa; line-height: 1.6; border-left: 3px solid rgba(192,57,43,0.3); }
.booking-note p { margin-bottom: 4px; }

@media (max-width: 1024px) { .booking-content { grid-template-columns: 1fr; } }
"""

# ─────────────────────────────────────────────
files["Payment.css"] = """\
.payment-page { padding: 40px 0; background: #0d0d0d; min-height: calc(100vh - 200px); }
.payment-container { max-width: 1000px; margin: 0 auto; }
.payment-header { background: #1a1a1a; padding: 24px; border-radius: 12px; margin-bottom: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.4); display: flex; justify-content: space-between; align-items: center; border: 1px solid #2a2a2a; }
.payment-header h1 { font-size: 32px; color: #f0f0f0; }
.countdown { display: flex; align-items: center; gap: 8px; font-size: 18px; color: #aaaaaa; }
.time { font-weight: bold; color: #e74c3c; font-size: 24px; }
.time.urgent { color: #ff4444; animation: pulse 1s infinite; }
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.5} }

.payment-content { display: grid; grid-template-columns: 1.2fr 1fr; gap: 24px; }

.booking-details { background: #1a1a1a; padding: 32px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.4); border: 1px solid #2a2a2a; }
.booking-details h2 { font-size: 24px; margin-bottom: 24px; color: #f0f0f0; }
.detail-section { margin-bottom: 24px; padding-bottom: 24px; border-bottom: 1px solid #2a2a2a; }
.detail-section:last-child { border-bottom: none; }
.detail-section h3 { font-size: 16px; color: #aaaaaa; margin-bottom: 12px; font-weight: 600; }
.movie-title { font-size: 20px; color: #e74c3c; font-weight: bold; margin-bottom: 12px; }
.detail-row { display: flex; justify-content: space-between; margin-bottom: 8px; color: #aaaaaa; }

.tickets-list { display: flex; flex-direction: column; gap: 8px; }
.ticket-item { display: flex; justify-content: space-between; align-items: center; padding: 12px; background: #111111; border-radius: 6px; border: 1px solid #2a2a2a; }
.ticket-seat { font-weight: bold; color: #e74c3c; }
.ticket-type { color: #666666; font-size: 14px; }
.ticket-price { font-weight: 600; color: #f0f0f0; }

.total-section { background: #111111; padding: 20px; border-radius: 8px; border: 1px solid rgba(192,57,43,0.2); }
.total-row { display: flex; justify-content: space-between; align-items: center; font-size: 18px; color: #dddddd; }
.total-amount { font-size: 28px; font-weight: bold; color: #e74c3c; }

.payment-methods { background: #1a1a1a; padding: 32px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.4); border: 1px solid #2a2a2a; }
.payment-methods h2 { font-size: 24px; margin-bottom: 24px; color: #f0f0f0; }
.payment-options { display: flex; flex-direction: column; gap: 12px; margin-bottom: 24px; }
.payment-option { display: flex; align-items: center; padding: 16px; border: 2px solid #2a2a2a; border-radius: 8px; cursor: pointer; transition: all 0.3s; background: #111111; }
.payment-option:hover { border-color: #c0392b; background: #1a0000; }
.payment-option.selected { border-color: #c0392b; background: rgba(192,57,43,0.08); }
.payment-option input[type="radio"] { margin-right: 12px; width: 20px; height: 20px; cursor: pointer; accent-color: #c0392b; }
.option-content { display: flex; align-items: center; gap: 12px; flex: 1; color: #dddddd; }
.option-icon { font-size: 24px; }
.option-name { font-weight: 600; color: #f0f0f0; }
.option-desc { font-size: 13px; color: #aaaaaa; }

.btn-pay {
  width: 100%; padding: 16px; background: linear-gradient(135deg, #c0392b 0%, #8b0000 100%);
  color: #f0f0f0; border: none; border-radius: 8px; font-size: 18px; font-weight: 700; cursor: pointer; transition: all 0.3s;
}
.btn-pay:hover:not(:disabled) { transform: translateY(-2px); box-shadow: 0 8px 24px rgba(192,57,43,0.4); background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%); }
.btn-pay:disabled { opacity: 0.4; cursor: not-allowed; }

@media (max-width: 768px) { .payment-content { grid-template-columns: 1fr; } }
"""

# ─────────────────────────────────────────────
files["Profile.css"] = """\
.profile-page { padding: 40px 0; min-height: calc(100vh - 200px); background: #0d0d0d; }
.profile-container { max-width: 800px; margin: 0 auto; background: #1a1a1a; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.5); overflow: hidden; border: 1px solid #2a2a2a; }
.profile-header { background: radial-gradient(ellipse at top, #2d0000 0%, #111111 100%); color: #f0f0f0; padding: 32px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(192,57,43,0.2); }
.profile-header h1 { font-size: 28px; }
.user-badge { display: flex; align-items: center; gap: 16px; background: rgba(192,57,43,0.15); padding: 12px 20px; border-radius: 8px; border: 1px solid rgba(192,57,43,0.2); }
.user-icon { font-size: 40px; }
.user-name { font-size: 20px; font-weight: bold; }
.user-role { font-size: 14px; color: #e74c3c; }

.profile-tabs { display: flex; border-bottom: 2px solid #2a2a2a; }
.tab-button { flex: 1; padding: 16px; background: none; border: none; font-size: 16px; font-weight: 600; color: #666666; cursor: pointer; transition: all 0.3s; border-bottom: 3px solid transparent; }
.tab-button:hover { color: #e74c3c; background: rgba(192,57,43,0.05); }
.tab-button.active { color: #e74c3c; border-bottom-color: #c0392b; }

.profile-form { padding: 32px; }
.password-requirements { background: #111111; border: 2px solid #2a2a2a; border-radius: 8px; padding: 16px; margin-bottom: 24px; }
.requirements-title { font-weight: 600; color: #dddddd; margin-bottom: 12px; font-size: 14px; }
.requirements-list { list-style: none; padding: 0; margin: 0; }
.requirements-list li { padding: 6px 0; color: #666666; font-size: 14px; transition: all 0.3s; }
.requirements-list li.valid { color: #27ae60; font-weight: 600; }

.form-group { margin-bottom: 20px; }
.form-group label { display: block; font-weight: 600; color: #dddddd; margin-bottom: 8px; font-size: 14px; }
.form-group input, .form-group select { width: 100%; padding: 12px 16px; border: 2px solid #2a2a2a; border-radius: 8px; font-size: 14px; transition: all 0.3s; background: #111111; color: #f0f0f0; }
.form-group input:focus, .form-group select:focus { outline: none; border-color: #c0392b; box-shadow: 0 0 0 3px rgba(192,57,43,0.12); }
.form-group input::placeholder { color: #555; }

.message { padding: 12px 16px; border-radius: 8px; margin-bottom: 20px; font-size: 14px; }
.message-success { background: rgba(39,174,96,0.1); color: #27ae60; border-left: 4px solid #27ae60; }
.message-error   { background: rgba(192,57,43,0.1); color: #e74c3c; border-left: 4px solid #c0392b; }

.btn-submit {
  width: 100%; padding: 14px; background: linear-gradient(135deg, #c0392b 0%, #8b0000 100%);
  color: #f0f0f0; border: none; border-radius: 8px; font-size: 16px; font-weight: 600; cursor: pointer; transition: all 0.3s;
}
.btn-submit:hover:not(:disabled) { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(192,57,43,0.4); background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%); }
.btn-submit:disabled { opacity: 0.5; cursor: not-allowed; }

@media (max-width: 768px) { .profile-header { flex-direction: column; gap: 16px; text-align: center; } .user-badge { width: 100%; justify-content: center; } }
"""

# ─────────────────────────────────────────────
files["BookingHistory.css"] = """\
.booking-history-page { padding: 40px 0; min-height: calc(100vh - 200px); background: #0d0d0d; }
.page-header { margin-bottom: 32px; }
.page-header h1 { font-size: 36px; color: #f0f0f0; }

.filter-section { display: flex; gap: 12px; margin-bottom: 24px; flex-wrap: wrap; }
.filter-btn { padding: 10px 20px; border: 2px solid #2a2a2a; background: #111111; border-radius: 8px; cursor: pointer; font-weight: 600; transition: all 0.3s; color: #aaaaaa; }
.filter-btn:hover { border-color: #c0392b; color: #e74c3c; }
.filter-btn.active { background: linear-gradient(135deg, #c0392b 0%, #8b0000 100%); color: #f0f0f0; border-color: transparent; }

.bookings-list { display: flex; flex-direction: column; gap: 20px; }
.booking-card { background: #1a1a1a; padding: 24px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.4); transition: all 0.3s; border: 1px solid #2a2a2a; }
.booking-card:hover { box-shadow: 0 4px 16px rgba(192,57,43,0.15); border-color: rgba(192,57,43,0.2); }

.booking-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #2a2a2a; }
.booking-title { display: flex; align-items: center; gap: 12px; }
.booking-title h3 { font-size: 20px; color: #f0f0f0; }
.booking-id { font-size: 12px; color: #555555; font-family: monospace; }

.status-badge { padding: 6px 12px; border-radius: 6px; font-size: 13px; font-weight: 600; }
.status-pending  { background: rgba(243,156,18,0.15); color: #f39c12; }
.status-reserved { background: rgba(52,152,219,0.15); color: #3498db; }
.status-paid     { background: rgba(39,174,96,0.15);  color: #27ae60; }
.status-canceled { background: rgba(192,57,43,0.15);  color: #e74c3c; }

.booking-details { margin-bottom: 16px; }
.detail-item { display: flex; gap: 12px; margin-bottom: 8px; color: #aaaaaa; }
.detail-label { font-weight: 600; min-width: 140px; color: #888888; }
.text-expired  { color: #e74c3c; font-weight: 600; }
.text-warning  { color: #f39c12; font-weight: 600; }
.time-remaining{ font-weight: bold; color: #e74c3c; }

.booking-tickets h4 { font-size: 14px; color: #666666; margin-bottom: 12px; }
.tickets-grid { display: flex; gap: 8px; flex-wrap: wrap; }
.ticket-badge { padding: 6px 12px; background: rgba(192,57,43,0.2); color: #e74c3c; border-radius: 6px; font-weight: 600; font-size: 13px; border: 1px solid rgba(192,57,43,0.3); }

.booking-footer { display: flex; justify-content: space-between; align-items: center; margin-top: 16px; padding-top: 16px; border-top: 1px solid #2a2a2a; }
.booking-total  { display: flex; gap: 12px; align-items: center; color: #aaaaaa; }
.total-amount   { font-size: 20px; font-weight: bold; color: #e74c3c; }
.booking-actions{ display: flex; gap: 12px; align-items: center; }

.btn-pay-now {
  padding: 10px 24px; background: linear-gradient(135deg, #c0392b 0%, #8b0000 100%);
  color: #f0f0f0; border: none; border-radius: 6px; font-weight: 600; font-size: 14px; cursor: pointer; transition: all 0.3s;
}
.btn-pay-now:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(192,57,43,0.4); background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%); }
.btn-cancel { padding: 10px 24px; background: transparent; color: #666666; border: 2px solid #333333; border-radius: 6px; font-weight: 600; font-size: 14px; cursor: pointer; transition: all 0.3s; }
.btn-cancel:hover { border-color: #e74c3c; color: #e74c3c; }

.empty-state { text-align: center; padding: 60px 20px; color: #555555; }
.empty-state p { font-size: 18px; margin-bottom: 20px; }
"""

# Write all files
for filename, content in files.items():
    path = os.path.join(BASE, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✅ {filename}")

print("\n🎨 Dark Red Cinema Theme applied to all CSS files!")
