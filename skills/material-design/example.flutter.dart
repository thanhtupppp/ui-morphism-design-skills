import 'package:flutter/material.dart';

class MaterialDesignCard extends StatelessWidget {
  const MaterialDesignCard({super.key});

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Material component', style: Theme.of(context).textTheme.titleMedium),
            const SizedBox(height: 12),
            const TextField(decoration: InputDecoration(labelText: 'Email')),
            const SizedBox(height: 12),
            FilledButton(onPressed: () {}, child: const Text('Save')),
          ],
        ),
      ),
    );
  }
}
