import discord

txt_error = ""
fatal_error = {'es-ES':"<:error:1055966710798237776> Fatal Error",
'en-US':"<:error:1055966710798237776> Fatal Error"}
color_embed_error = 0xff0000

failed_icons = {'en-US':"Failed to generate icons, please try again. \n \n<:levelinfo:1055963416327634954> If this continues to occur, report it to the [ObeyGDBot Support Server](https://discord.gg/ZbXNrk349b).",
'es-ES':"Error al generar los iconos, intentalo de nuevo. \n \n<:levelinfo:1055963416327634954> Si esto sigue ocurriendo, reportalo al servidor de [Soporte de ObeyGDBot](https://discord.gg/ZbXNrk349b)."}

error_servers = {'es-ES':'Ha ocurrido un error al obtener información a los servidores de Geometry Dash, intenta de nuevo en unos minutos...',
'en-US':'An error occurred while getting information from the Geometry Dash servers, try in a few minutes...'}
cssembederror = {'es-ES':f"```diff\n- {error_servers['es-ES']} \n```",
'en-US':f"```diff\n- {error_servers['en-US']} \n```"}
error_gduser_txt = {'en-US':f"{cssembederror['en-US']} \n<:question:982857313180332032> **Geometry Dash Servers are working?** Check that you have written everything correctly and try again. \n\n<:levelinfo:1055963416327634954> If this continues to occur, report it to the [ObeyGDBot Support Server](https://discord.gg/ZbXNrk349b)."
,'es-ES':f"{cssembederror['es-ES']} \n<:question:982857313180332032> **¿Los servidores de Geometry Dash están funcionando?** Comprueba que lo escribiste todo correctamente e intentalo nuevamente. \n\n<:levelinfo:1055963416327634954> Si esto sigue ocurriendo, reportalo al servidor de [Soporte de ObeyGDBot](https://discord.gg/ZbXNrk349b)."}
error_command_txt = {'en-US':"An error occurred while trying to run this command, try again or report it to [ObeyGDBot Support Server](https://discord.gg/ZbXNrk349b).",
'es-ES':"Ha ocurrido un error al intentar ejecutar este comando, intente de nuevo o reportelo en el [Servidor de Soporte de ObeyGDBot](https://discord.gg/ZbXNrk349b)."
}
error_gdser = {'en-US':discord.Embed(title=f'{fatal_error["en-US"]}',description=f'{error_gduser_txt["en-US"]}',color=color_embed_error),
'es-ES':discord.Embed(title=f'{fatal_error["es-ES"]}',description=f'{error_gduser_txt["es-ES"]}',color=color_embed_error)}
error_command = {'en-US':discord.Embed(title=f'{fatal_error["en-US"]}',description=f'{error_command_txt["en-US"]}',color=color_embed_error),
'es-ES':discord.Embed(title=f'{fatal_error["es-ES"]}',description=f'{error_command_txt["es-ES"]}',color=color_embed_error)}
#gdsettings
gdset_title = {'en-US':"Change my background profile",
'es-ES':"Cambiar mi fondo de perfil"}
gdset_desc = {'en-US':"Select a custom image background for your _Geometry Dash profile_. \n<:accountfriends:888338801330647080>_Anyone will be able to view your personalized background that you have selected!_",
'es-ES':"Selecciona un fondo para tu _perfil de Geometry Dash._ \n<:accountfriends:888338801330647080> **¡Cualquier persona pueda ver tu fondo personalizado que seleccionaste!**"}
gdset_desc_vip = {'es-ES':"Para obtener los fondos VIP debes unirte al Servidor de ObeyGDBOT.",
'en-US':"Get VIP backgrounds joining in ObeyGDBOT Discord Server."}
getset_desc_premiun = {'es-ES':"Para obtener los fondos prémium debes haber realizado una donación.",
'en-US':'Get Premium backgrounds making a donation.'}
getset_desc_final = {'es-ES':"\n<:download:1055963541573738546> **¡Desliza la barra de selección para encontrar más fondos!**",
'en-US':"\n<:download:1055963541573738546> **Slide the selection bar to find more backgrounds!**"}
getset_txt_selected = {'en-US':"We hope you like your new background!",
'es-ES':"¡Esperemos que te guste tu nuevo fondo!"}
getset_txt_selected_premiun = {'en-US':"Almost!!!\n\n<:GJ_sTrendingIcon_001:896652962435301376> Upload your background with the `/profile backgrounds premium` command!",
'es-ES':"¡Ya está casi todo listo!\n\n<:GJ_sTrendingIcon_001:896652962435301376> ¡Sube tu fondo con el comando `/profile backgrounds premiun`!"}
getset_txt_custom = {'en-US':"A custom background, personalized by you!",
'es-ES':"¡Un fondo completamente personalizado por ti!"}
getset_txt_freetrial = {'en-US':"You have a free trial to use VIP and Premium backgrounds!",
'es-ES':"¡Tienes una prueba gratuita para usar fondos VIP y Premium!"}
getset_txt_free = {'en-US':"",
'es-ES':""}
getset_txt_premiun = {'en-US':"3 Random Backgrounds!",
'es-ES':"3 Fondos completamente aleatorios!"}
getset_txt_gdps = {'en-US':"Special GDPS background!",
'es-ES':"Fondo único del GDPS!"}
getset_txt_vip = {'en-US':"VIP Background",
'es-ES':"Fondo VIP"}
gdset_txt_special = {'en-US':"Current event",
'es-ES':"Evento actual"}
gdset_txt_special_none = {'en-US':"None event current! :(",
'es-ES':"¡No hay eventos! :("}
gdset_button_global = {'en-US':"Default brown background for unlinked accounts!",
'es-ES':"Fondo marrón por defecto para cuentas no vinculadas!"}
#Premium addon
gdset_image_preview = {'en-US':"Image Preview",
'es-ES':"Vista previa de la imagen"}
#Premium error
gdset_image_error_upload = {'en-US':"Error uploading image.",
'es-ES':"Error al subir la imagen."}
gdset_image_error_size = {'en-US':"Image size big! Limited at 1.5MB for image.",
'es-ES':"Tamaño de imagen demasiado grande! Limite de subida: 1.5MB por imagen."}
gdset_image_error_format = {'en-US':"Image height or width is very little! \nRecommended: 1360x760, Minimum: 160x320",
'es-ES':"¡La altura o anchura de la imagen es demasiado pequeña! \nRecomendado: 1360x760, Minímo: 160x320"}
gdset_image_error_unsupported = {'en-US':"Error, this file is not a image supported! \nRecommended: JPG & JPEG",
'es-ES':"Error, este archivo no es una imagen compatible! \nRecomendado: JPG & JPEG"}
#######
gdset_sucess = {'en-US':"Has been selected correctly",
'es-ES':"¡Seleccionado correctamente!"}
gdset_error_color_bg = {'en-US':"Unknown background",
'es-ES':"Fondo desconocido"}
######
#SPECIAL CHANGES
getset_brown = {'en-US':"Brown",
'es-ES':"Marrón"}
getset_blue = {'en-US':"Blue",
'es-ES':"Azul"}
getset_green = {'en-US':"Green",
'es-ES':"Verde"}
getset_red = {'en-US':"Red",
'es-ES':"Rojo"}
getset_pink = {'en-US':"Rosed/Pink",
'es-ES':"Rosa/Rosado"}
getset_purple = {'en-US':"Purple",
'es-ES':"Purpura"}
getset_orange = {'en-US':"Orange",
'es-ES':"Naranja"}
getset_yellow = {'en-US':"Yellow",
'es-ES':"Amarillo"}
getset_grey = {'en-US':"Grey",
'es-ES':"Gris"}
getset_black = {'en-US':"Black",
'es-ES':"Negro"}
getset_special = {'en-US':"[EVENTS] Background FREE of events!",
'es-ES':"[EVENTOS] ¡Fondo GRATIS de eventos!"}
getset_special_rainbow = {'en-US':"[VIP] Rainbow",
'es-ES':"[VIP] Arcoíris"}
getset_custom = {'en-US':"[Premium] Custom Background",
'es-ES':"[Premium] Fondo Personalizado"}
getset_special_michigun = {'en-US':"[VIP] Michigun",
'es-ES':"[VIP] Michigun"}
getset_special_snow_2021 = {'en-US':"[VIP] Snowdown 2021",
'es-ES':"[VIP] Nevada/Navidad 2021"}
getset_special_snow_2022 = {'en-US':"[VIP] Snowdown 2022",
'es-ES':"[VIP] Nevada/Navidad 2022"}
getset_special_anniversary = {'en-US':"[VIP] 9th GD Anniversary",
'es-ES':"[VIP] 9no Aniversario de GD"}
getset_special_newyear_2023 = {'en-US':"[VIP] Happy new year 2023!",
'es-ES':"[VIP] ¡Feliz año nuevo 2023!"}
getset_special_halloween = {'en-US':"[VIP] Halloween",
'es-ES':"[VIP] Halloween/Noche de brujas"}
getset_gdps_zombiedash = {'en-US':"[GDPS] Zombie Dash"}
getset_gdps_gdpseditor22 = {'en-US':"[GDPS] GDPS Editor 2.2"}
getset_hidden_1 = {'en-US':"Happy day of the Innocents!",
'es-ES':"¡Feliz día de los inocentes!"}
getset_special_heartbreaker_2023 = {'en-US':"[VIP] Heartbreaker",
'es-ES':"[VIP] Rompecorazones"}
##Siempre poner los hidden al final
getset_colors = {"_default":{
    'en-US':getset_brown['en-US'],
    'es-ES':getset_brown['es-ES']
    },
"_blue":{
    'en-US':getset_blue['en-US'],
    'es-ES':getset_blue['es-ES']
    },
"_green":{
    'en-US':getset_green['en-US'],
    'es-ES':getset_green['es-ES']
    },
"_red":{
    'en-US':getset_red['en-US'],
    'es-ES':getset_red['es-ES']
    },
"_pink":{
    'en-US':getset_pink['en-US'],
    'es-ES':getset_pink['es-ES']
    },
"_purple":{
    'en-US':getset_purple['en-US'],
    'es-ES':getset_purple['es-ES']
    },
"_orange":{
    'en-US':getset_orange['en-US'],
    'es-ES':getset_orange['es-ES']
    },
"_yellow":{
    'en-US':getset_yellow['en-US'],
    'es-ES':getset_yellow['es-ES']
    },
"_grey":{
    'en-US':getset_grey['en-US'],
    'es-ES':getset_grey['es-ES']
    },
"_black":{
    'en-US':getset_black['en-US'],
    'es-ES':getset_black['es-ES']
    },
"_special":{
    'en-US':getset_special['en-US'],
    'es-ES':getset_special['es-ES']
    },
"_custom":{
    'en-US':getset_custom['en-US'],
    'es-ES':getset_custom['es-ES']
    },
"_special_heartbreaker_2023":{
    'en-US':getset_special_heartbreaker_2023['en-US'],
    'es-ES':getset_special_heartbreaker_2023['es-ES']
    },
"_special_halloween":{
    'en-US':getset_special_halloween['en-US'],
    'es-ES':getset_special_halloween['es-ES']
    },
"_special_snow_2022":{
    'en-US':getset_special_snow_2022['en-US'],
    'es-ES':getset_special_snow_2022['es-ES']
    },
"_special_snow":{
    'en-US':getset_special_snow_2021['en-US'],
    'es-ES':getset_special_snow_2021['es-ES']
    },
"_special_newyear_2023":{
    'en-US':getset_special_newyear_2023['en-US'],
    'es-ES':getset_special_newyear_2023['es-ES']
    },
"_special_anniversary":{
    'en-US':getset_special_anniversary['en-US'],
    'es-ES':getset_special_anniversary['es-ES']
    },
"_special_michigun":{
    'en-US':getset_special_michigun['en-US'],
    'es-ES':getset_special_michigun['es-ES']
    },
"_special_rainbow":{
    'en-US':getset_special_rainbow['en-US'],
    'es-ES':getset_special_rainbow['es-ES']
    },
"_gdps_gdpseditor22":{
    'en-US':getset_gdps_gdpseditor22['en-US'],
    'es-ES':getset_gdps_gdpseditor22['en-US']
    },
"_gdps_zombiedash":{
    'en-US':getset_gdps_zombiedash['en-US'],
    'es-ES':getset_gdps_zombiedash['en-US']
    },
"_hidden_1":{
    'en-US':getset_hidden_1['en-US'],
    'es-ES':getset_hidden_1['es-ES']
    }
}

#SPECIAL CHANGES END
getset_selected_txt = {'en-US':"Background currently selected:",
'es-ES':"Fondo actualmente seleccionado:"}
gdset_title_global = {'en-US':"Global profile settings",
'es-ES':"Configuración global de perfiles"}
gdset_desc_global = {'en-US':"Select a specific background for the other Geometry Dash profiles. \nThis setting only applies to you!",
'es-ES':"Selecciona un fondo determinado para los demás perfiles de Geometry Dash. \n¡Esta configuración solamente aplica para ti!"}
#Colors
gdset_colors_support = {'en-US':"Color palette availables:",
'es-ES':"Paleta de colores disponibles:"}
gdset_colors_select = {'en-US':"Select your color palette",
'es-ES':"Selecciona tu paleta de colores"}
gdset_colors_desc = {'en-US':"**Android:** [Italian Apk Downloader](https://www.youtube.com/c/italianapkdownloader) _(Android Mod Menu)_\n**Windows:** [Sai](https://www.youtube.com/channel/UCvYEPVUVVLDhwfHCzgVdIIg) _(DLL/Sai Mod Pack)_ \n**Windows/iOS/Android:** [Robtop Games](https://www.youtube.com/robtopgames) _(Official)_"}
gdset_colors_glow_button = {'en-US':"Set principal color for glow",
'es-ES':"Colocar color principal como glow"}
#Premium/VIP BG
gdset_nopremiun = {'en-US':"Unlock this **Premium Background**, make a vote with the command `/vote` and get a free premium trial or make an donation in [ObeyGDBOT Discord Support Server](https://discord.gg/ZbXNrk349b).",
'es-ES':"Para poder desbloquear este **Fondo Premium** debes realizar una votación con el comando `/vote` o realiza una donación en el [Servidor de ObeyGDBOT](https://discord.gg/ZbXNrk349b)."}
gdset_novip = {'en-US':"Unlock this **VIP Background**, get be level 10 (XP Chat) on the [ObeyGDBOT Discord Support Server](https://discord.gg/ZbXNrk349b).",
'es-ES':"Para poder desbloquear este **Fondo VIP** debes ser nivel 10 de experiencia de chat en el [Servidor de ObeyGDBOT](https://discord.gg/ZbXNrk349b)."}
gdset_nogdps = {'en-US':"Unlock this **GDPS Background**, creating and linking an account in the selected GDPS with ObeyGDBOT.",
'es-ES':"Para poder desbloquear este **Fondo GDPS** debes crear y vincular una cuenta en el GDPS Seleccionado con ObeyGDBOT."}
##Premium uploads
gdset_upload_sucess = {'en-US':"<:woaaa:1004293455029215262> Congratulations, your new background is now available on your profile!",
'es-ES':"<:woaaa:1004293455029215262> ¡Felicidades, tu nuevo fondo ya está disponible en tu perfil!"}
gdset_upload_queue = {'en-US':"<:levelinfo:1055963416327634954> **Confirming your background you agree:**\n:underage: Do not upload images for adults (NSFW +18).\n:no_entry_sign: Do not upload grotesque images.\n:no_mobile_phones: Do not upload images that violate Discord's terms and services.\n<:markalert:888594454473240597> **Violating our terms of use results in a permanent ban on this command.**",
'es-ES':"<:levelinfo:1055963416327634954> **Al confirmar tu fondo usted acepta:**\n:underage: No subir imágenes para adultos (NSFW +18).\n:no_entry_sign: No subir imágenes grotecas.\n:no_mobile_phones: No subir imágenes que incumplan los términos y servicios de Discord.\n<:markalert:888594454473240597> **Incumplir con estos requisitos provocará estar baneado permanentemente de este comando.**"}


#Slash
s_typ = {'en-US':"ObeyGDBot is thinking...",
'es-ES':"ObeyGDBot está pensando..."}
s_sea = {'en-US':"<a:time_loading:983361962459136050> **Searching results...**",
'es-ES':"<a:time_loading:983361962459136050> **Buscando resultados...**"}
#Selectbar
s_select_bar = {'en-US':"Select your choice here!",
'es-ES':"Escoge una opción aquí"}


#Queque
q_title = {'en-US':"In queue...",
'es-ES':"En cola de espera..."}
q_des = {'en-US':"*The queue is used to avoid overloading the {} servers*",
'es-ES':"*La cola de espera sirve para no sobrecargar los servidores de {}*"}
q_button_left = {'en-US':"Leave queue",
'es-ES':"Abandonar cola de espera"}
q_cancelled_title = {'en-US':"Queue canceled!",
'es-ES':"¡Cola de espera abandonada!"}
q_queue_limit = {'en-US':"Queue limit reached, please wait a few minutes before using this command again.",
'es-ES':"Se alcanzó el limite para entrar a la cola de espera, por favor espera unos minutos antes de usar este comando nuevamente."}
q_delete_error = {'en-US':"Unexpected error...",
'es-ES':"Error inesperado..."}

#Global
gl_lengsucess = {'en-US':"Se ha seleccionado correctamente el lenguaje, este cambio se aplicará la próxima vez que use un comando.",
'es-ES':"The language has been selected correctly, this change will be applied later."}
gl_loading_command = {'en-US':"<a:time_loading:983361962459136050> **Loading command...**",
'es-ES':"<a:time_loading:983361962459136050> **Cargando el comando...**"}
gl_sucess = {'en-US':"Success",
'es-ES':"Éxitoso"}
gl_cancelled = {'en-US':"Cancelled",
'es-ES':"Cancelado"}
gl_confirm = {'en-US':"Confirm",
'es-ES':"Confirmar"}
gl_cancel = {'en-US':"Cancel",
'es-ES':"Cancelar"}
gl_rank = {'en-US':"Rank:",
'es-ES':"Posición:"}
gl_time = {'en-US':"Estimated time:",
'es-ES':"Tiempo Estimado:"}
gl_enabled = {'en-US':"<:sucess:1055966393805324438>`Enabled`",
'es-ES':"<:sucess:1055966393805324438>`Sí`"}
gl_disabled = {'en-US':"<:error:1055966710798237776>`Disabled`",
'es-ES':"<:error:1055966710798237776>`No`"}
gl_only_friends = {'en-US':"<:positionicon:911684444753109063>`Only Friends`",
'es-ES':"<:positionicon:911684444753109063>`Sólo amigos`"}
gl_loading = {'en-US':"Loading...",
'es-ES':"Cargando..."}
gl_parte = {'en-US':"Part",
'es-ES':"Parte"}
gl_friendreq = {'en-US':"Friend req. :",
'es-ES':"Solicitudes:"}
gl_chathis = {'en-US':"Chat history:",
'es-ES':"Historial:"}
gl_messages = {'en-US':"Messages:",
'es-ES':"Mensajes:"}
gl_alert_disabled = {'en-US':"Alert disabled",
'es-ES':"Alerta deshabilitada"}
gl_alert_enabled = {'en-US':"Disable this alert!",
'es-ES':"Desactivar esta alerta!"}
gl_no_premiun = {'en-US':"You are not a premium user, you must vote with the `/vote` command or make a donation on the [ObeyGDBOT Server](https://discord.gg/ZbXNrk349b).",
'es-ES':"No eres usuario prémium, debes realizar una votación con el comando `/vote` o realiza una donación en el [Servidor de ObeyGDBOT](https://discord.gg/ZbXNrk349b)."}

#Global no json
gl_warningleng = "<:leng:916255681718386689> Your lenguage is not supported, English set for default. \n Change it with command: "
gl_errorleng = "An error has occurred in the language."

#account link -> Geometry Dash
acc_l_msg = {'en-US':"Your verification code is:",
'es-ES':"Tu codigo de verificacion es:"}
#account link -> Discord
acc_l_title = {'en-US':"Your code sent!",
'es-ES':"¡Codigo de verificación enviado!"}
acc_l_des = {'en-US':"**Your verification code has been sent!**\nCheck the messages in your Geometry Dash account to read your code\n<:accountp01:888338398090264616> **To verify your code you must write the command in Discord:** `/account code (and your verification code)` \n\n<:markalert:888594454473240597> **ObeyGDBot will never ask for personal information and we do NOT ask for passwords to register.**",
'es-ES':"**¡Se ha enviado tu código de verificación!**\nRevisa los mensajes en tu cuenta de Geometry Dash para leer tu código\n<:accountp01:888338398090264616> **Para verificar tu código debes escribir el comando en Discord:** `/account code (y tu código de verificación)` \n\n<:markalert:888594454473240597> **ObeyGDBot jamás pedirá información personal y NO pedimos contraseñas para registrarse.**"}
acc_l_usernotis = {'en-US':"<:levelinfo:1055963416327634954> If you misplaced your Geometry Dash name or did not receive the code within Geometry Dash you can remove the existing code with the `/account unlink` command and retry the link.",
'es-ES':"<:levelinfo:1055963416327634954> Si colocaste mal tu nombre de Geometry Dash o no recibiste el código dentro de Geometry Dash puedes eliminar el código existente con el comando `/account unlink` y volver a intentar la vinculación."}
acc_l_errorlink = {'en-US':"**You have a linked account with OGDB**, unlink your account with the command `/account unlink`",
'es-ES':"**Tienes una cuenta vinculada con OGDB**, desvincula tu cuenta con el comando `/account unlink`"}
acc_l_errorsend = {'en-US':"You have already sent a code, check your messages in Geometry Dash!",
'es-ES':"¡Ya has enviado un código, revisa tus mensajes en Geometry Dash!"}
acc_l_erroruser = {'en-US':"**This Geometry Dash profile not exist (in {})!**\nMake sure you type the *username* correctly or you can also enter your *Geometry Dash Account ID* if your _username_ contains invalid characters.",
'es-ES':"**¡Este perfil de Geometry Dash no existe (en {})!**\nAsegurate de escribir correctamente el *nombre del perfil* o también puede colocar su *ID de su cuenta* si es que el _username_ contiene carácteres inválidos."}
acc_l_errormsg = {'en-US':"**You do not have messages enabled in your Geometry Dash account!** \n\n<:markalert:888594454473240597>  *OGDB can't send you our verification code, follow these steps to enable messages for your account:*",
'es-ES':"**¡Tienes los mensajes sólo para amigos o están deshabilitados en tu cuenta de Geometry Dash!** \n\n<:markalert:888594454473240597>  *No se puede enviar nuestro código de verificación, sigue estos pasos para habilitar los mensajes de tu cuenta:*"}

#account code
acc_c_succeslink_title = {'en-US':"Your account has been linked!",
'es-ES':"¡Se ha vinculado tu cuenta!"}
acc_c_succeslink_desc = {'en-US':"Your Geometry Dash account was linked to ObeyGDBot \n \n<:levelinfo:1055963416327634954> _You can now use ObeyGDBot commands more easily!_",
'es-ES':"Se vinculó tu cuenta de Geometry Dash con ObeyGDBot \n \n<:levelinfo:1055963416327634954> _¡Ya puedes usar los comandos de ObeyGDBot más facilmente!_"}
acc_c_errorlimit = {'en-US':"You have exceeded the limit of bad code attempts! \nYou will need to send the code again with the command:",
'es-ES':"¡Has superado el límite de intentos de códigos erroneós! \nNecesitarás de nuevo enviar el código con el comando:"}
acc_c_errorlink = {'en-US':"Your verification code is wrong! \n \n<:levelinfo:1055963416327634954> If your code contains letters, please write them exactly the same with corresponding upper and lower case.",
'es-ES':"¡No coincide tu código de verificacion! \n \n<:levelinfo:1055963416327634954> Si tú codigo contiene letras, escribelo exactamente igual con sus mayúsculas y minúsculas correspondientes."}
acc_c_errorlinkedacc = {'en-US':"You have a linked account, you don't need to use this command again.",
'es-ES':"Tienes una cuenta vinculada, no hace falta usar este comando de nuevo."}
acc_c_errornoinfo = {'en-US':"This command is to enter the verification code and link your Geometry Dash account with ObeyGDBot, use the command: `/account link` to receive a verification code.",
'es-ES':"Este comando es para ingresar el código de verificación y vincular tu cuenta de Geometry Dash con ObeyGDBot, utilice el comando: `/account link` para recibir un código de verificación."}

#account unlink
acc_u_initial = {'en-US':"Unlinking your Geometry Dash account with ObeyGDBot",
'es-ES':"Desvinculando cuenta de Geometry Dash con ObeyGDBot"}
acc_u_cancel = {'en-US':"Unlinking your Geometry Dash account with ObeyGDBot cancelled!",
'es-ES':"Desvinculación de tu cuenta de Geometry Dash con ObeyGDBot cancelado!"}
acc_u_unlinkquestion = {'en-US':"Are you sure to **unlink** your Geometry Dash account of _ObeyGDBot_?",
'es-ES':"¿Está seguro de **desvincular** su cuenta de Geometry Dash de _ObeyGDBot_?"}
acc_u_unlinkquestion_code = {'en-US':"Are you sure to **delete** your account link code from _ObeyGDBot_?",
'es-ES':"¿Está seguro de **eliminar** su código para vincularse con _ObeyGDBot_?"}
acc_u_errorunlink = {'en-US':"You do not have any account linked to ObeyGDBot, if you want to link account use the command",
'es-ES':"No posees ninguna cuenta vinculada con ObeyGDBot, si desea vincular una cuenta utilice el comando"}
acc_u_succesunlink = {'en-US':"Your Geometry Dash profile has been successfully unlinked from ObeyGDBot",
'es-ES':"Se ha desvinculado correctamente tu perfil de Geometry Dash de ObeyGDBot"}

#Profile Alerts
p_alert_txt_1 = {'en-US':"**Don't like the background you currently have?** \nChange it with the command",
'es-ES':"**¿No te gusta el fondo que tienes actualmente?** \nCambialo con el comando"}
p_alert_txt_2 = {'en-US':"**Are you using a color palette and your colors icons not match?** \nSetup with command",
'es-ES':"**¿Estás usando una paleta de colores y no son los colores de tus iconos?** \nConfiguralo con el comando"}

#C_Profile
p_error_comm = {'en-US':"<:markalert:888594454473240597> **You need to put a username!**\n<:slash:915203820097794058> *Example:* `/profile gd ObeyGDBOT` \n\n<:levelinfo:1055963416327634954> Link your Geometry Dash account with ObeyGDBot to access this command more easily. *Command:* `/account link`.",
'es-ES':"<:markalert:888594454473240597> **¡Necesitas poner un nombre de usuario!**\n<:slash:915203820097794058> *Ejemplo:* `/profile gd ObeyGDBOT` \n\n<:levelinfo:1055963416327634954> Vincula tu cuenta de Geometry Dash con ObeyGDBot con el comando `/account link` para usar este comando fácilmente."}
p_error_user = {'en-US':"<:levelinfo:1055963416327634954> If the problem persists make sure **the servers are working**.",
'es-ES':"<:levelinfo:1055963416327634954> Si el problema persiste asegurate que **los servidores estén funcionando**."}
p_error_user_discord = {'en-US':"<:markalert:888594454473240597> **{} is not linked with ObeyGDBOT!**\n\n<:levelinfo:1055963416327634954> **Invite him to link account with the command:** `/account link`.",
'es-ES':"<:markalert:888594454473240597> **¡{} no está vinculado con ObeyGDBOT!**\n\n<:levelinfo:1055963416327634954> **Invitalo a vincular su cuenta con el comando:** `/account link`."}
p_l_des = {'en-US':"Generating icons and obtaining statistics...",
'es-ES':"Generando iconos y obteniendo estadisticas..."}
p_l_searching = {'en-US':"Searching profile...",
'es-ES':"Buscando perfil..."}
p_time_txt = {'en-US':"Approximate time remaining: ",'es-ES':"Tiempo restante aproximado: "}
p_title = {'en-US':"Statistics and generated icons",
'es-ES':"Estadísticas e iconos generados"}
p_field = {'en-US':"Profile settings",'es-ES':"Configuraciones del perfil"}
p_des = {'en-US':"Profile of",'es-ES':"Perfil de"}
p_footer = {'en-US':"Statistics and icons are updated",
'es-ES':"Las estadisticas y iconos se actualizarán"}
#C_Profile Unused
p_imgtime = {'en-US':"Image generated in",
'es-ES':"Imagen generada en"}
p_warnicon = {'en-US':"Icons not found: ",
'es-ES':"Iconos no encontrados: "}
p_warncol = {'en-US':"Colors not found (Color Palett): ",
'es-ES':"Colores no encontrados (Color Palett): "}
p_colorpalette = {'en-US':"`Color palette compatible`",
'es-ES':"`Paleta de colores compatible`"}
#querylevelid
qlid_demonlist = {'en-US':"on Demon List",
'es-ES':"en la Demon List"} 
qlid_txt_verify = {'en-US':"Verified by",
'es-ES':"Verificado por"}
qlid_txt_verifyvideo = {'en-US':"Verification Video",
'es-ES':"Video de verificación"}
qlid_downsong = {'en-US':"Download Song",
'es-ES':"Descargar Canción"}
qlid_newgrounds = {'en-US':"Newgrounds",
'es-ES':"Newgrounds"}
qlid_youtube = {'en-US':"Youtube",
'es-ES':"Youtube"}
qlid_comp = {'en-US':"Compatible with {} version or higher.",
'es-ES':"Compatible con la versión {} o superior."}
qlid_starsreq = {'en-US':"Stars Requested:",
'es-ES':"Estrellas solicitadas:"}
qlid_error_noinfo = {'en-US':"No more information about this level.\n<:levelinfo:1055963416327634954> If the problem persists, verify that the servers are working.",
'es-ES':"No hay más información acerca de este nivel.\n<:levelinfo:1055963416327634954> Si el problema persiste verifica que los servidores estén funcionando."}
qlid_errordes = {'en-US':"Search levels more easily with command",
'es-ES':"Busca niveles más facilmente con el comando"}

#querylevelget
qlget_norel = {'en-US':"Without results...",
'es-ES':"Sin resultados..."}
qlget_nomorerel = {'en-US':"No more results...",
'es-ES':"No hay más resultados..."}
qlget_title = {'en-US':"Searching:",
'es-ES':"Busquedas con:"}
qlget_desc = {'en-US':"Pages:",
'es-ES':"Pagina(s):"}

#SupportMe
supp_desc = {'en-US':"**Support ObeyGDBot voting on Top.gg!**\n\n<:love:985352429279256596> Vote for ObeyGDBot and receive **VIP/Premium free trials** every 12 hours.",
'es-ES':"**¡Apoyame votando en Top.gg!**\n\n<:love:985352429279256596> Vota por ObeyGDBot y recibe **pruebas gratis de VIP/Premium** cada 12 horas."}
supp_button = {'en-US':"Vote here!",
'es-ES':"¡Vota aquí!"}
supp_check_button = {'en-US':"Check my vote and claim rewards!",
'es-ES':"¡Revisar mi voto para reclamar recompensas!"}
supp_sucess = {'en-US':"<:GJ_sMagicIcon_001:912480293640884294> Congratulations you have claimed your reward and you can use any VIP/Premium Background, you can claim another one within 12 hours!",
'es-ES':"<:GJ_sMagicIcon_001:912480293640884294> ¡Felicidades has reclamado tu recompensa y puedes usar cualquier Fondo VIP/Premium, puedes reclamar otro dentro de 12 horas!"}
supp_error = {'en-US':"<:error:1055966710798237776> Make sure you have voted on top.gg with your user {}#{}!",
'es-ES':"<:error:1055966710798237776> ¡Asegurate que has votado en top.gg con tu usuario {}#{}!"}
supp_error_timestamp = {'en-US':"<:levelinfo:1055963416327634954> You've voted before, wait again <t:{}:R>!",
'es-ES':"<:levelinfo:1055963416327634954> ¡Ya has votado anteriormente, espera de nuevo <t:{}:R>!"}
supp_error_timeout = {'en-US':"You have taken too long to verify your vote, if you have already voted just verify your vote again.",
'es-ES':"Has tardado demasiado en verificar tu voto, si ya has votado únicamente invoca este comando nuevamente."}

#GenerateCollab
gc_i_txt = {'en-US':"Collab hosted by",
'es-ES':"Colaboración hosteado por"}
gc_i_txt1 = {'en-US':"**Level name:** \n **Level music:**",
'es-ES':"**Nombre del nivel:** \n **Música del nivel:**"}
gc_f_txt = {'en-US':"Copy and paste the messages, if you need to modify it manually.",
'es-ES':"Copia y pega los mensajes, si requieres modificarlo manualmente."}
gc_txt = {'en-US':"\n\n**Initial Triggers:** \n`Group 1.- Alpha 0%` \n`Group 2.- Alpha 50%` \n\n**Initial Colors:** \n`Color 1.-` :black_circle: `Black` \n`Color 2.-` :white_circle: `White` \n\n",
'es-ES':"\n\n**Triggers Iniciales:** \n`Grupo 1.- Alpha 0%` \n`Grupo 2.- Alpha 50%` \n\n**Colores Iniciales:** \n`Color 1.-` :black_circle: `Negro` \n`Color 2.-` :white_circle: `Blanco` \n\n"}
gc_error_limit = {'en-US':"Member limit exceeded.",
'es-ES':"Límite de miembros superado."}

#Buttons
b_err = {'en-US':"You cannot interact with this message, only the author can do this!",
'es-ES':"¡No puedes interactuar con este mensaje, solamente el autor puede hacer esto!"}

#Handler Errors
error_no_owner_gdps = {'en-US':"<:error:1055966710798237776> This Discord guild does not own any GDPS",
'es-ES':"<:error:1055966710798237776> Este servidor de Discord no es dueño de algún GDPS"}
error_private_message = {'en-US':"<:error:1055966710798237776> You can't run this command because you're not in a Discord guild",
'es-ES':"<:error:1055966710798237776> No puedes ejecutar este comando debido a que no estás en un servidor de Discord"} 
error_cd_desc = {'en-US':"<:timeico:1055965254032576513> You have wait {} to use `/{}` again",
'es-ES':"<:timeico:1055965254032576513> Tienes que esperar {} para volver a usar el comando `/{}`"}
error_limitint_desc = {'en-US':"<:error:1055966710798237776> You have reached the limit of interactions with this command.",
'es-ES':"<:error:1055966710798237776>Has alcanzado el límite de interacciones con este comando."} 
error_admin_per = {'en-US':"You cannot interact with this command because you are not an administrator of this Discord guild.",
'es-ES':"No puedes interactuar con este comando por qué no eres administrador de éste servidor de Discord."}
error_nocommand_per = {'en-US':"You can't interact with this command because you don't have permission to use it on this Discord guild.",
'es-ES':"No puedes interactuar con este comando por qué no tienes permiso de usarlo en éste servidor de Discord."}
error_unknown = {'en-US':"Unknown error, please report with code: {}",
'es-ES':"Error desconocido, porfavor de reportar con el código: {}"}
error_rate_limit = {'en-US':"**I have a limitation in Discord, please wait a few moments before use again: ** `/{}`\n<:penoso:1004293694486224908> If it happens again **report it** to the [ObeyGDBOT Discord Support Server](https://discord.gg/ZbXNrk349b) with error code: `{}`",
'es-ES':"**Tengo una limitación por parte de Discord, porfavor espera unos momentos antes de volver a usar el comando:** `/{}`\n<:penoso:1004293694486224908> Si ocurre de nuevo **reportalo** en el [Servidor de ObeyGDBOT](https://discord.gg/ZbXNrk349b) con el código de error: `{}`"
}
error_global = {'en-US':"**An error occurred while interacting with command** `/{}`\n<:penoso:1004293694486224908> If it happens again **report it** to the [ObeyGDBOT Discord Support Server](https://discord.gg/ZbXNrk349b) with error code: `{}`",
'es-ES':"**Ocurrió un error al hacer interacción con el comando** `/{}`\n<:penoso:1004293694486224908> Si ocurre de nuevo **reportalo** en el [Servidor de ObeyGDBOT](https://discord.gg/ZbXNrk349b) con el código de error: `{}`"
}
error_invoke = {'en-US':"**An error occurred while trying to invoke the command:** `/{}`\n<:penoso:1004293694486224908> If it happens again **report it** to the [ObeyGDBOT Discord Support Server](https://discord.gg/ZbXNrk349b) with error code: `{}`",
'es-ES':"**Ocurrió un error al intentar invocar el comando:** `/{}`\n<:penoso:1004293694486224908> Si ocurre de nuevo **reportalo** en el [Servidor de ObeyGDBOT](https://discord.gg/ZbXNrk349b) con el código de error: `{}`"
}
gdset_error_time = {'en-US':"Time to select expired!",
'es-ES':"¡El tiempo para poder seleccionar una opción ha expirado!"}
gdset_failed = {'en-US':"Failed to select option!",
'es-ES':"¡Error al seleccionar la opción!"}
gdset_errorverify = {'en-US':"You don't have an account linked to ObeyGDBot. \n\nLink account now with <:slash:915203820097794058> **command:**",
'es-ES':"No tienes una cuenta vinculada a ObeyGDBot. \n\nVincula uno ahora con el <:slash:915203820097794058> **comando:**"}#Only special

#Badges
bdg_title = {'en-US':"Badges",
'es-ES':"Insignias"}
bdg_original_desc = {'en-US':"Verified account",
'es-ES':"Cuenta verificada"}
bdg_patner_desc = {'en-US':"OGDB Patner",
'es-ES':"Patrocinador de OGDB"}
bdg_creator_desc = {'en-US':"Featured Creator",
'es-ES':"Creador destacado"}
bdg_mod_desc = {'en-US':"Moderator",
'es-ES':"Moderador"}
bdg_donator_desc = {'en-US':"OGDB Donator",
'es-ES':"OGDB Donador"}
bdg_stargrinder_desc = {'en-US':"Star Grinder",
'es-ES':"Farmeador de Estrellas"}
bdg_fixer_desc = {'en-US':"OGDB Bug Hunter",
'es-ES':"Cazaerrores de OGDB"}

#LEVEL LENGS
lvl_pages_title = {'en-US':"Showing levels: {} of {}",
'es-ES':"Mostrando niveles: {} de {}"}
lvl_pages_subtitle = {'en-US':"Page: {} of {}",
'es-ES':"Pagina: {} de {}"}
lvl_txt_desc = {'en-US':"(No description provided)",
'es-ES':"(No se proporcionó descripción)"}

#Guild tools
g_tools_title = {'en-US':"GDPS Tools",
'es-ES':"Herramientas del GDPS"}
g_tools_desc = {'en-US':"Here you can find all the tools that can help you in this GDPS!",
'es-ES':"¡Aquí puedes encontrar todas las herramientas que pueden servirte de ayuda en el GDPS!"}

#Guild settings
g_sett_sucess = {'en-US':"Guild settings saved successfully.",
'es-ES':"Configuraciones del servidor guardadas con éxito."}
g_sett_title = {'en-US':"Choice an config. option",
'es-ES':"Selecciona una opción a configurar"}
g_sett_description_embed = {'en-US':"<:levelinfo:1055963416327634954> The embed title is limited to 256 characters and the embed description to 4000 characters and the image URL only in HTTPS:JPG/PNG format\n\n<:levelinfo:1055963416327634954> You can add users to admin commands only from ObeyGDBOT **(but it doesn't give them admin on the server)** -> You must add the user IDs separated by `,` -> Example: `806057353920249866,401472259128164353`",
'es-ES':"<:levelinfo:1055963416327634954> El titulo del embed está limitado a 256 caracteres y la descripción del embed a 4000 caracteres y la URL de imagen únicamente en formato HTTPS:JPG/PNG\n\n<:levelinfo:1055963416327634954> Puedes agregar usuarios a comandos de administrador únicamente de ObeyGDBOT **(pero no les da administrador en el servidor)** -> Debes agregar los IDs de los usuarios separado por `,` -> Ejemplo: `806057353920249866,401472259128164353`"}
g_sett_description_endpoint = {'en-US':"<:levelinfo:1055963416327634954> `endpoint` -> Requested file located on the root page ending with file extension -> PHP/HTML -> Example: `tools/test.php`",
'es-ES':"<:levelinfo:1055963416327634954> `endpoint` -> Archivo a que se hace petición ubicado de la página raíz terminando con la extención del archivo -> PHP/HTML -> Ejemplo: `tools/test.php`"}
g_sett_description_alias = {'en-US':"<:levelinfo:1055963416327634954> `url_alias` -> ID of the fields that sends the information in `ID:NEWID` format separated by `,` -> Example: `name:levelname,id_level:levelid`",
'es-ES':"<:levelinfo:1055963416327634954> `url_alias` -> ID de los campos que envía la información en formato `ID:NEWID` separado por `,` -> Ejemplo: `name:levelname,id_level:levelid`"}
g_sett_description_hexcolor = {'en-US':"<:color_palete:979886804822020147> `embed_color` -> Color only HEX format -> Example: `#FFFFFF`",
'es-ES':"<:color_palete:979886804822020147> `embed_color` -> Color únicamente el formato HEX -> Ejemplo: `#FFFFFF`"}
g_sett_description_warning = {'en-US':"<:markalert:888594454473240597> Don't modify it if you don't know what you're doing!",
'es-ES':"<:markalert:888594454473240597> ¡No lo modifique si no sabe lo que hace!"}

#GDPS Tools
gt_title_songr = {'en-US':"Song Reupload",
'es-ES':"Resubir una canción"}
gt_title_whorated = {'en-US':"Know who rated level",
'es-ES':"Saber quién calificó un nivel"}
gt_loading_songr = {'en-US':"Reuploading song...",
'es-ES':"Resubiendo la canción..."}

#Modals -> Any Error
moda_error_expired = {'en-US':"<:error:1055966710798237776> Time to complete the form expired!",
'es-ES':"<:error:1055966710798237776> ¡Tiempo para acompletar el formulario expiró!"}

#Modals -> Any
moda_response_any_sucess = {'en-US':"Settings saved!",
'es-ES':"¡Configuraciones guardadas con éxito!"}
moda_title_any = {'en-US':"Setting",
'es-ES':"Configuración"}
moda_response_any_error = {'en-US':"Error 404: File error!",
'es-ES':"¡Error 404: Error de archivos!"}

#Modals -> URLSettings
moda_response_url_error = {'en-US':"URL invalid!",
'es-ES':"¡La URL es inválido!"}
moda_response_format_error = {'en-US':"Alias format invalid!",
'es-ES':"¡Formato de alias inválido!"}

#Modals -> Webhook
moda_response_webhook_sucess = {'en-US':"Webhook setting saved!",
'es-ES':"¡Configuraciones del Webhook guardadas con éxito!"}
moda_response_webhook_error = {'en-US':"Webhook url invalid!",
'es-ES':"¡La URL de Webhook es inválido!"}
moda_response_webhook_disabled = {'en-US':"Webhook disabled!",
'es-ES':"¡Webhook desactivado!"}

#Modals -> WhoRated
moda_init_title_whorated = {'en-US':"Know who rated level",
'es-ES':"Saber quién calificó un nivel"}
moda_title_whorated = {'en-US':"Level ID",
'es-ES':"ID del nivel"}
moda_response_whorated_sucess = {'en-US':"The person who rated the level was",
'es-ES':"La persona que calificó el nivel fué"}
moda_response_whorated_failed = {'en-US':"GDPS Internal Server Error",
'es-ES':"GDPS Internal Server Error"}
#Modals -> Song reupload
moda_title_song = {'en-US':"Song name",
'es-ES':"Nombre de la canción"}
moda_title_song_url = {'en-US':"URL for MP3 song",
'es-ES':"URL de la canción MP3"}
moda_value_song_url = {'en-US':"Youtube song uploads are slow. (Only URLs of",
'es-ES':"Las descargas de Youtube son lentas. (Solo se permiten URLs de"}
moda_response_song_sucess = {'en-US':"**Song reuploaded**",
'es-ES':"**Música resubida**"}
moda_response_song_failed_url = {'en-US':"Invalid URL or Unsupported URL",
'es-ES':"URL inválido o URL no soportado"}
moda_response_song_failed_size = {'en-US':"The YouTube song is too long.",
'es-ES':"La canción de YouTube es demasiado largo."}
moda_response_song_failed_format = {'en-US':"The song is not in an .MP3 format",
'es-ES':"La canción no tiene un formato .MP3"}
moda_response_song_failed_server = {'en-US':"Internal server error in GDPS",
'es-ES':"Error interno del servidor en el GDPS"}
moda_response_song_failed_yt = {'en-US':"Error trying reuploading YouTube song to GDPS",
'es-ES':"Error al intentar resubir la canción de Youtube al GDPS"}
moda_response_song_failed = {'en-US':"Error when trying to upload the song to the GDPS",
'es-ES':"Error al intentar subir la canción en el GDPS"}
moda_downloading_yt = {'en-US':"Trying to reupload song from YouTube... \n<:levelinfo:1055963416327634954> This may take a few seconds...",
'es-ES':"Intentando resubir la canción desde YouTube... \n<:levelinfo:1055963416327634954> Esto puede tardar unos segundos..."}

#No perms
perm_server_maint = {'en-US':"<a:cuberotate:879306691705974854> ObeyGDBOT is undergoing maintenance, please try again in a few minutes...",
"es-ES":"<a:cuberotate:879306691705974854> ObeyGDBOT está en mantenimiento, inténtalo de nuevo en unos minutos..."
}
perms_user_banned = {'en-US':"<:cry:1004294281101594677> Your account is **banned** from ObeyGDBOT because you violated the terms of use.\n<:levelinfo:1055963416327634954> _If you consider it's a wrong, you can appeal in the ObeyGDBot Support Server:_ https://discord.gg/ZbXNrk349b",
'es-ES':"<:cry:1004294281101594677> Tu cuenta está **baneada** de ObeyGDBOT porque incumpliste los términos de uso.\n<:levelinfo:1055963416327634954> _Si crees que es un error puedes apelarlo en el Servidor de Soporte de ObeyGDBot:_ https://discord.gg/ZbXNrk349b"
}
perms_user_verifyaccount = {'en-US':"<:error:1055966710798237776> You must have a linked Geometry Dash account to use this command.\n<:levelinfo:1055963416327634954> Use the `/account link` command to link an account.",
'es-ES':"<:error:1055966710798237776> Necesitas tener vinculado una cuenta de Geometry Dash para poder usar este comando.\n<:levelinfo:1055963416327634954> Utiliza el comando `/account link` para vincular una cuenta."}

# for datas in getset_colors.items():
#     name,txt = datas
#     print(name, txt)
