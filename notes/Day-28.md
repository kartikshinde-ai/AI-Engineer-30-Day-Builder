# Day 28 – MCP Introduction

## Goal

The goal of Day 28 was to understand the basic idea of MCP (Model Context Protocol), why it exists, and how it relates to the tools built in Project 4.

## What is MCP?

MCP (Model Context Protocol) is a standard way for AI applications to interact with external tools and resources.

Instead of every AI application needing a different custom integration for every tool or data source, MCP provides a common interface for connecting AI applications with tools and resources.

## Problem MCP Solves

AI applications often need access to external capabilities such as:

- Tools
- Data
- Resources
- Services

Without a common standard, integrations can become different and difficult to maintain.

MCP provides a standardized way for an AI application to discover and use these capabilities.

## Main Components

### MCP Client

The MCP Client is the part of an AI application that connects to an MCP server.

It can discover available capabilities and communicate with the server.

### MCP Server

An MCP Server exposes capabilities to an AI application through the MCP interface.

These capabilities can include tools and resources.

### Tool

A tool is an action that an AI application can call to perform a specific operation.

For example:

- Search FAQ
- Get leads
- Generate a draft

### Resource

A resource provides information or data that an AI application can access.

Resources can represent information such as documents, files, or other data sources.

## Simple MCP Architecture

```text
AI Application
      |
      v
  MCP Client
      |
      v
  MCP Server
      |
      v
  FAQ Search Tool
      |
      v
 FAQ Knowledge Base