import Link from "next/link";

const trips = [
  { id: "1", title: "杭州三日游" },
  { id: "2", title: "成都五日游" },
];

export default function TripsPage() {
  return (
    <main>
      <h1>我的行程</h1>

      <ul>
        {trips.map((trip) => (
          <li key={trip.id}>
            <Link href={`/trips/${trip.id}`}>
              {trip.title}
            </Link>
          </li>
        ))}
      </ul>
    </main>
  );
}