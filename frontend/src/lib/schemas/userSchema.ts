import { z } from 'zod';

/* Update User */
export const updateUserSchema = z.object({
    name: z.string().min(1, {message: 'Nome é obrigatório'}).max(80, {message: 'Nome deve ter no máximo 80 caracteres'}),
    email: z.string().email({message: 'E-mail inválido'}).max(254, {message: 'E-mail deve ter no máximo 254 caracteres'}),
    password: z.string()
                .refine(value => !value || /^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[^a-zA-Z0-9\s]).+$/.test(value), 
                        {message: 'Senha deve conter pelo menos 1 letra, 1 número e 1 caractere especial'}),
    confirm_password: z.string(),
}).refine(data => data.password === data.confirm_password, {
    message: 'As senhas não conferem',
    path: ['confirm_password']
})

export type UpdateUserSchemaType = z.infer<typeof updateUserSchema>