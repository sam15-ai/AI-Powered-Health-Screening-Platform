import { Link } from 'react-router-dom'


const features = [
  {
    title: 'Symptom Checker',
    description:
      'Turn everyday symptoms into a fast preliminary screening backed by AI-assisted pattern recognition.',
  },
  {
    title: 'Image Diagnosis',
    description:
      'Upload skin images for an instant first-pass analysis that can help prioritize clinical follow-up.',
  },
  {
    title: 'Health History',
    description:
      'Review past screenings, urgency levels, and suggested next steps from one organized dashboard.',
  },
]

function Landing() {
  return (
    <main className="relative overflow-hidden">
      <div className="absolute inset-x-0 top-0 -z-10 h-[32rem] bg-[radial-gradient(circle_at_20%_20%,rgba(56,189,248,0.18),transparent_32%),radial-gradient(circle_at_80%_18%,rgba(147,197,253,0.28),transparent_28%)]" />

      <section className="mx-auto flex max-w-6xl flex-col gap-16 px-6 py-16 md:py-24">
        <div className="grid items-center gap-12 lg:grid-cols-[1.15fr_0.85fr]">
          <div>
            <div className="inline-flex items-center gap-2 rounded-full border border-sky-200 bg-white/85 px-4 py-2 text-sm font-medium text-sky-700 shadow-sm shadow-sky-100">
              <span className="h-2.5 w-2.5 rounded-full bg-emerald-500" />
              AI health support for underserved communities
            </div>
            <h1 className="mt-8 max-w-3xl text-5xl font-semibold tracking-tight text-slate-950 md:text-7xl">
              HealthScreen AI
            </h1>
            <p className="mt-6 max-w-2xl text-xl leading-8 text-slate-600">
              Free AI-powered health screening for everyone
            </p>
            <p className="mt-6 max-w-2xl text-base leading-8 text-slate-500">
              Bring symptom assessment, skin-image screening, and health history
              tracking into a simple experience designed to lower access barriers
              and support timely follow-up care.
            </p>

            <div className="mt-10 flex flex-col gap-4 sm:flex-row">
              <Link
                to="/register"
                className="inline-flex items-center justify-center rounded-full bg-sky-600 px-7 py-4 text-base font-semibold text-white shadow-xl shadow-sky-200 transition hover:bg-sky-700"
              >
                Get Started
              </Link>
              <Link
                to="/about"
                className="inline-flex items-center justify-center rounded-full border border-sky-200 bg-white px-7 py-4 text-base font-semibold text-sky-700 transition hover:border-sky-300 hover:bg-sky-50"
              >
                Learn More
              </Link>
            </div>
          </div>

          <div className="relative">
            <div className="rounded-[2rem] border border-sky-100 bg-white/90 p-8 shadow-[0_30px_90px_rgba(14,116,144,0.12)]">
              <div className="grid gap-4">
                <div className="rounded-3xl bg-sky-50 p-5">
                  <p className="text-sm font-semibold uppercase tracking-[0.25em] text-sky-600">
                    Rapid Access
                  </p>
                  <p className="mt-3 text-2xl font-semibold text-slate-900">
                    Screening support in minutes, not hours
                  </p>
                </div>
                <div className="grid gap-4 sm:grid-cols-2">
                  <div className="rounded-3xl bg-slate-900 p-5 text-white">
                    <p className="text-sm text-sky-200">Symptom Pathway</p>
                    <p className="mt-2 text-3xl font-semibold">24/7</p>
                    <p className="mt-2 text-sm text-slate-300">
                      Always-available preliminary checks
                    </p>
                  </div>
                  <div className="rounded-3xl bg-sky-600 p-5 text-white">
                    <p className="text-sm text-sky-100">Image Workflow</p>
                    <p className="mt-2 text-3xl font-semibold">5 Classes</p>
                    <p className="mt-2 text-sm text-sky-50">
                      Skin-analysis model starter pipeline
                    </p>
                  </div>
                </div>
                <div className="rounded-3xl border border-slate-200 bg-white p-5">
                  <p className="text-sm font-semibold text-slate-500">
                    Built for compassionate triage
                  </p>
                  <p className="mt-2 text-base leading-7 text-slate-700">
                    Clear urgency guidance, specialist recommendations, and
                    patient-friendly flows reduce uncertainty at the first point
                    of care.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <section className="grid gap-6 md:grid-cols-3">
          {features.map((feature) => (
            <article
              key={feature.title}
              className="rounded-[1.75rem] border border-sky-100 bg-white/90 p-8 shadow-[0_24px_64px_rgba(14,116,144,0.08)]"
            >
              <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-sky-100 text-lg font-bold text-sky-700">
                {feature.title
                  .split(' ')
                  .map((word) => word[0])
                  .join('')}
              </div>
              <h2 className="mt-6 text-2xl font-semibold tracking-tight text-slate-900">
                {feature.title}
              </h2>
              <p className="mt-4 text-base leading-8 text-slate-600">
                {feature.description}
              </p>
            </article>
          ))}
        </section>
      </section>
    </main>
  )
}

export default Landing
