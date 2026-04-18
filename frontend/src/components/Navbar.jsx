import { useEffect, useState } from 'react'
import { Link, NavLink, useLocation, useNavigate } from 'react-router-dom'


const navLinks = [
  { label: 'Home', to: '/' },
  { label: 'Symptom Checker', to: '/symptom-checker' },
  { label: 'Image Diagnosis', to: '/image-diagnosis' },
  { label: 'Dashboard', to: '/dashboard' },
]

function Navbar() {
  const [isAuthenticated, setIsAuthenticated] = useState(
    Boolean(localStorage.getItem('token')),
  )
  const location = useLocation()
  const navigate = useNavigate()

  useEffect(() => {
    setIsAuthenticated(Boolean(localStorage.getItem('token')))
  }, [location.pathname])

  const handleLogout = () => {
    localStorage.removeItem('token')
    setIsAuthenticated(false)
    navigate('/login')
  }

  return (
    <header className="sticky top-0 z-20 border-b border-white/70 bg-white/80 backdrop-blur-xl">
      <div className="mx-auto flex max-w-6xl items-center justify-between gap-6 px-6 py-4">
        <Link to="/" className="flex items-center gap-3">
          <div className="flex h-11 w-11 items-center justify-center rounded-2xl bg-sky-600 text-lg font-bold text-white shadow-lg shadow-sky-200">
            HS
          </div>
          <div>
            <p className="text-lg font-semibold tracking-tight text-slate-900">
              HealthScreen AI
            </p>
            <p className="text-xs font-medium uppercase tracking-[0.25em] text-sky-600">
              Community-first screening
            </p>
          </div>
        </Link>

        <nav className="hidden items-center gap-2 rounded-full border border-sky-100 bg-sky-50/80 px-2 py-2 md:flex">
          {navLinks.map((link) => (
            <NavLink
              key={link.to}
              to={link.to}
              className={({ isActive }) =>
                `rounded-full px-4 py-2 text-sm font-medium transition ${
                  isActive
                    ? 'bg-sky-600 text-white shadow-md shadow-sky-200'
                    : 'text-slate-600 hover:bg-white hover:text-sky-700'
                }`
              }
            >
              {link.label}
            </NavLink>
          ))}
        </nav>

        <div className="flex items-center gap-3">
          {isAuthenticated ? (
            <button
              type="button"
              onClick={handleLogout}
              className="rounded-full border border-sky-200 px-5 py-2.5 text-sm font-semibold text-sky-700 transition hover:border-sky-300 hover:bg-sky-50"
            >
              Logout
            </button>
          ) : (
            <>
              <Link
                to="/login"
                className="rounded-full px-4 py-2 text-sm font-semibold text-slate-700 transition hover:bg-slate-100"
              >
                Login
              </Link>
              <Link
                to="/register"
                className="rounded-full bg-sky-600 px-5 py-2.5 text-sm font-semibold text-white shadow-lg shadow-sky-200 transition hover:bg-sky-700"
              >
                Register
              </Link>
            </>
          )}
        </div>
      </div>
    </header>
  )
}

export default Navbar
