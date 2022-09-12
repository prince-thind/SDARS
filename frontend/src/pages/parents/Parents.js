import UnauthorizedAccess from "../../lib/commonComponents/UnauthorisedAccess"
import CircularsSection from "../../lib/commonComponents/CircularsSection";
import ProgressSection from "./components/ProgressSection";
import Attendence from "./components/AttendenceSection";
import FeeSection from "./components/FeeSection";


export default function Parents({ username, privilege }) {
    if (!username || !privilege) return <UnauthorizedAccess />

    return <div>
        <CircularsSection />
        <ProgressSection username={username} />
        <Attendence username={username}/>
        <FeeSection username={username}/>

    </div>
}