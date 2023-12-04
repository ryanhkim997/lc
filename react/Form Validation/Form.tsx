import React, { useState } from "react";
import { Input } from "./Input";
import { validateEmail } from "./utils";

import "./style.css";
import { ErrorMsg } from "./ErrorMsg";

interface IError {
  firstName: string | null;
  lastName: string | null;
  email: string | null;
  password: string | null;
}

export default function Form() {
  const [fields, setFields] = useState({
    firstName: "",
    lastName: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  const [errors, setErrors] = useState<IError>({
    firstName: null,
    lastName: null,
    email: null,
    password: null,
  });

  const [success, setSuccess] = useState(false);

  function handleFieldChange(field, value) {
    setFields({
      ...fields,
      [field]: value,
    });
  }

  function handleSubmit(e) {
    let hasErrors = false;
    let errorObj: IError = {
      firstName: null,
      lastName: null,
      email: null,
      password: null,
    };
    setSuccess(false);
    setErrors(errorObj);
    e.preventDefault();

    if (fields.firstName.length < 3) {
      errorObj.firstName = "First Name cannot be less than 3 characters";
      hasErrors = true;
    }
    if (fields.lastName.length < 3) {
      errorObj.lastName = "Last Name cannot be less than 3 characters";
      hasErrors = true;
    }
    if (!validateEmail(fields.email)) {
      errorObj.email = "Email address is invalid";
      hasErrors = true;
    }
    if (fields.password !== fields.confirmPassword) {
      errorObj.password = "Passwords do not match";
      hasErrors = true;
    }

    if (hasErrors) {
      setErrors(errorObj);
      return;
    }

    setSuccess(true);
  }

  return (
    <form
      onSubmit={(e) => {
        handleSubmit(e);
      }}
    >
      <>
        <Input
          label="First Name"
          value={fields.firstName}
          setField={(firstName: string) =>
            handleFieldChange("firstName", firstName)
          }
        />
        {console.log(errors)}
        {errors.firstName && <ErrorMsg message={errors.firstName} />}
        <Input
          label="Last Name"
          value={fields.lastName}
          setField={(lastName: string) =>
            handleFieldChange("lastName", lastName)
          }
        />
        {errors.lastName && <ErrorMsg message={errors.lastName} />}
        <Input
          label="Email"
          value={fields.email}
          setField={(email: string) => handleFieldChange("email", email)}
        />
        {errors.email && <ErrorMsg message={errors.email} />}
        <Input
          label="Password"
          value={fields.password}
          setField={(password: string) =>
            handleFieldChange("password", password)
          }
        />
        <Input
          label="Confirm Password"
          value={fields.confirmPassword}
          setField={(confirmPassword: string) =>
            handleFieldChange("confirmPassword", confirmPassword)
          }
        />
        {errors.password && <ErrorMsg message={errors.password} />}
        <input type="submit" value="Register"></input>
        {success && <div>Form has been submitted successfully!</div>}
      </>
    </form>
  );
}
