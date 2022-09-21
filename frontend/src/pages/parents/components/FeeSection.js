import { useEffect, useState } from "react"
import { fetchFees } from "../../../lib/API";

export default function FeeSection({ username }) {
    const [fees, setFees] = useState([]);

    useEffect(() => {
        fetchFees(username).then(e => {
            setFees(e)
        })
    }, [username])


    return <section className="module">
        <h3>Fees</h3>
        {fees.length === 0 ? "loading" : ""}
        <ul>
            {fees.map(e => {
                return <li key={e.id}><FeeCard feeElement={e} /></li>
            })}
        </ul>
    </section>
}

function FeeCard({ feeElement }) {
    return <div className="module-item">
        <h4>Name:  {feeElement.name}</h4>
        <h4>Cost: {feeElement.cost}</h4>
        <p>{feeElement.description}</p>
    </div>
}
