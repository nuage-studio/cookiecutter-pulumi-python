# Pulumi Dynamic Provider Template example

This folder contains an example Pulumi program which uses the `pulumi-acme` example
project to create a dummy "Database" resource.  You should replace this with an example
of your dynamic provider being used, using this README as a template.

## Getting started

To run this example:

* Install and start a VirtualEnv in this folder
* Locally install (or reinstall) the `pulumi-acme` package from the root directory:

```
pip install -e ..
```

* Optionally set your provider configuration:

```
pulumi config set provider_param_1 [value]
pulumi config set provider_param_2 [value]
```

* Deploy the stack:

```
pulumi up
```
