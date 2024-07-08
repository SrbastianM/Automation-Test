Feature: Login Functionally
    Scenario:  Login successful (user & password)
      Given El usuario ingresó a la plataforma
      When El usuario ingresa sus credenciales
      And El usuario hace clic en el botón ingresar
      Then El usuario es redirigido a la página de inicio o home
      And El usuario visualiza el mensaje de bienvenida
      And El usuario cierra sesión

   Scenario: Login unsuccessful (user & password)
      Given El usuario ingresó a la plataforma
      When El usuario ingresa sus credenciales de manera incorrecta
      And El usuario hace clic en el botón ingresar
      Then El usuario visualiza el mensaje de credenciales incorrectas