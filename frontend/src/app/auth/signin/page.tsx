import { SignInPage } from "@/components/pages/signin";
import { Metadata } from "next";

export const metada: Metadata = {
    title: "Logar-se"
}

const SignIn = () => <SignInPage />;

export default SignIn;