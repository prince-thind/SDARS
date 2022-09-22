import { useState } from "react";
import { submitAttedence } from "../../../lib/API";
import Error from "../../../lib/commonComponents/ErrorToast";

export default function AttedenceSection() {
    const [error, setError] = useState(null)
    const [res, setRes] = useState(null)

    return <form className="form module" onSubmit={handleSubmit}>
        <h3>Upload Attedence</h3>
        <div className="container">
            <label>Enter Username: <input type="text" required name="username"></input> </label>
            <label>Enter Attedence: <input type="number" required name="attedence" value="100"></input> </label>
            <label>Enter Remakrs: <input type="text" name="remarks" value="N/A"></input> </label>
        </div>
        <button>Submit</button>
        {error && <Error error={error} />}
        {res && <div className="success">{res}</div>}
    </form>;

    async function handleSubmit(e) {
        e.preventDefault();
        setRes(null)
        setError(null)
        const form = e.target;
        const values = Object.fromEntries(new FormData(form).entries())

        const status = await submitAttedence(values);
        if (status) {
            setRes('Uploaded')
        }
        else {
            setError('Error Uploading')
        }

    }
}

