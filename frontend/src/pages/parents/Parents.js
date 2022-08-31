import UnauthorizedAccess from "../../lib/commonComponents/UnauthorisedAccess"

export default function Parents({ username, privilege }) {
    if (!username || !privilege) return <UnauthorizedAccess />

    return <div>parents</div>
}