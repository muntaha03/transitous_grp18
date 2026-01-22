<!--
SPDX-License-Identifier: CC0-1.0
SPDX-FileCopyrightText: none
-->

<p align="center">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="website/static/images/logo-text.svg" width="400">
        <source media="(prefers-color-scheme: light)" srcset="website/static/images/logo-text-dark.svg" width="400">
        <img src="website/static/images/logo-text-dark.svg" alt="Transitous" width="400"><br>
    </picture>
</p>

<p align="center">
    <b>Free and open public transport routing.</b>
</p>

## Goal

A community-run provider-neutral international public transport routing service.

Using openly available GTFS/GTFS-RT/etc. feeds and FOSS routing engine we want to operate a
routing service that:  

* focuses on the interest of the user rather than the public transport operators
* is free to use
* values user privacy
* does not stop at borders
* aims at crowd-sourced maintenance of data feeds in the spirit of FOSS

## Contact

For general discussions about data availability: [#opentransport:matrix.org](https://matrix.to/#/#opentransport:matrix.org)

For Transitous-specific technical topics: [#transitous:matrix.spline.de](https://matrix.to/#/#transitous:matrix.spline.de)

Also, follow <a href="https://en.osm.town/@transitous" rel="me">Transitous on Mastodon</a>.

## Configuring Transitous

Transitous is configured using *regions*. A region tells Transitous which public-transport data feeds belong to a certain area (for example a country or city).

At a high level:

- Each region is defined by a **JSON file** in the `feeds/` directory.
- The file name usually follows the ISO country or subdivision code (for example `DE.json` for Germany).
- A region file normally contains:
  - a list of **maintainers** for that region’s data. 
  - a list of **sources** (GTFS, real-time feeds, etc.) that should be fetched for the region.

This configuration is what Transitous uses to know where to download data from and which areas it can route in.

## Continuous integration & deployment

This repository uses GitHub Actions to automate testing and deployment through the **SME Continuous Integration** workflow.

### **Workflow details**
- **Trigger**: The pipeline is automatically initiated on every `push` or `sync` to the `main` branch.
- Upon successful testing a `deployment-package` is generated as a build artifact.

### **How to monitor**
1. Navigate to the **Actions** tab in the GitHub repository.
2. Select the latest run titled **"SME Continuous Integration"**.
3. Verify the **build and test** and **deploy-artifact** jobs have successfully completed.

For detailed examples of region files and all supported source types, see the documentation on the  [Project Website](https://transitous.org/doc/#adding-a-region).