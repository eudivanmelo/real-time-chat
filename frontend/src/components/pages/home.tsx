"use client";

import { useChatStore } from "@/stores/chatStore";
import { Chat } from "../chat";
import Image from "next/image";
import HomeSectionBG from "@/assets/home-section-bg.png"

export const HomePage = () => {
    const { chat, setShowNewChat } = useChatStore()

    return (
        <div className="h-app">
            {chat ?
                <Chat />
            :
                <div className="flex flex-col items-center gap-12 py-8 h-full px-4">
                    <div className="flex flex-col items-center justify-center gap-12 flex-1">
                        <Image 
                            src={HomeSectionBG}
                            alt="Home Section"
                            width={440}
                            priority
                        />

                        <p className="text-xl max-w-xl text-center font-bold text-slate-600 dark:text-slate-300">
                            Por favor, selecione uma conversa para visualizar as
                            mensagens ou inicie uma nova conversa.
                        </p>
                    </div>
                </div>
            }
        </div>
    )
}