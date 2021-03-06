// Code generated by go-swagger; DO NOT EDIT.

package models

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"encoding/json"

	strfmt "github.com/go-openapi/strfmt"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/validate"
)

// V2StatusResponse v2 status response
// swagger:model v2StatusResponse
type V2StatusResponse string

const (

	// V2StatusResponseOK captures enum value "OK"
	V2StatusResponseOK V2StatusResponse = "OK"

	// V2StatusResponseError captures enum value "Error"
	V2StatusResponseError V2StatusResponse = "Error"
)

// for schema
var v2StatusResponseEnum []interface{}

func init() {
	var res []V2StatusResponse
	if err := json.Unmarshal([]byte(`["OK","Error"]`), &res); err != nil {
		panic(err)
	}
	for _, v := range res {
		v2StatusResponseEnum = append(v2StatusResponseEnum, v)
	}
}

func (m V2StatusResponse) validateV2StatusResponseEnum(path, location string, value V2StatusResponse) error {
	if err := validate.Enum(path, location, value, v2StatusResponseEnum); err != nil {
		return err
	}
	return nil
}

// Validate validates this v2 status response
func (m V2StatusResponse) Validate(formats strfmt.Registry) error {
	var res []error

	// value enum
	if err := m.validateV2StatusResponseEnum("", "body", m); err != nil {
		return err
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}
