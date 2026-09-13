import 'package:flutter/material.dart';

class MaterialDesignDemo extends StatelessWidget {
  const MaterialDesignDemo({super.key, this.onSave});

  final VoidCallback? onSave;

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    return Card(
      elevation: 1,
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Material component', style: theme.textTheme.titleMedium),
            const SizedBox(height: 12),
            const TextField(
              decoration: InputDecoration(
                labelText: 'Email',
                helperText: 'We will use this for notifications.',
              ),
            ),
            const SizedBox(height: 12),
            Wrap(
              spacing: 12,
              runSpacing: 8,
              children: [
                OutlinedButton(onPressed: () {}, child: const Text('Cancel')),
                FilledButton(
                  onPressed: onSave,
                  style: FilledButton.styleFrom(minimumSize: const Size(44, 44)),
                  child: const Text('Save'),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
