#!/bin/bash

# Get the latest tag with the "client-v0." prefix
latest_tag=$(git tag --list "client-v0.*" | sort -V | tail -n 1)

# If no previous tags found, use default version
if [ -z "$latest_tag" ]; then
  latest_tag="client-v0.0"
fi

# Extract the current version number and propose the next minor version
current_version=$(echo "$latest_tag" | grep -oP 'client-v0.\K\d+')
next_version=$((current_version + 1))
proposed_tag="client-v0.${next_version}"

# Prompt user for a tag name
echo "Latest tag: $latest_tag"
read -p "Enter the new tag name (proposed: ${proposed_tag}): " new_tag
new_tag=${new_tag:-$proposed_tag}

# Create the .tar.gz archive
mkdir -p dist
tar czvf dist/wnc_client.tar.gz unix_client/*

# Prompt for release title and description
default_release_title="Client release ${new_tag}"
default_release_description="Client release ${new_tag}"
read -p "Enter the release title (default: ${default_release_title}): " release_title
release_title=${release_title:-$default_release_title}
read -p "Enter the release description (default: ${default_release_description}): " release_description
release_description=${release_description:-$default_release_description}


# Ask for confirmation before creating the tag, pushing it, and creating the release
echo "New tag: ${new_tag}"
echo "Release title: ${release_title}"
echo "Release description: ${release_description}"
read -p "Proceed with creating the release? (y/N): " confirmation

case $confirmation in
  [Yy]* )
    # Create the new tag and push it to the remote repository
    git tag "$new_tag"
    git push origin "$new_tag"

    # Create the GitHub release
    gh release create "$new_tag" --title "$release_title" --notes "$release_description"

    # Attach the wnc_client.tar.gz file to the release
    gh release upload "$new_tag" dist/wnc_client.tar.gz

    echo "Release created successfully."
    ;;
  * )
    echo "Release creation canceled."
    ;;
esac

