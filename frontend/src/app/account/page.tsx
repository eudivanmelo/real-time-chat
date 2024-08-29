import { AccountPage } from "@/components/pages/account";
import { Metadata } from "next";

export const metadata: Metadata = {
    title: "Perfil"
}

const Account = () => <AccountPage />;

export default Account;