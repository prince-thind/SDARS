import UnauthorizedAccess from "../../lib/commonComponents/UnauthorisedAccess"

export default function Teachers({ username, privilege }) {
    if (!username || !privilege) return <UnauthorizedAccess />

    return <div>Teachers</div>
}