import 'package:flutter/material.dart';

class BentoExample extends StatelessWidget {
  const BentoExample({super.key});

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        final columns = constraints.maxWidth >= 1024
            ? 4
            : constraints.maxWidth >= 720
                ? 2
                : 1;

        return GridView.builder(
          padding: const EdgeInsets.all(16),
          gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: columns,
            crossAxisSpacing: 16,
            mainAxisSpacing: 16,
            mainAxisExtent: constraints.maxWidth < 720 ? 180 : 160,
          ),
          itemCount: 4,
          itemBuilder: (context, index) {
            final titles = ['Hero', 'Supporting', 'Utility', 'Detail'];
            final descriptions = [
              'Primary product or outcome.',
              'Secondary information.',
              'Quick action or compact metric.',
              'A richer chart, preview, or detail module.',
            ];

            return Card(
              clipBehavior: Clip.antiAlias,
              child: Padding(
                padding: const EdgeInsets.all(20),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(titles[index], style: Theme.of(context).textTheme.titleLarge),
                    const SizedBox(height: 8),
                    Expanded(child: Text(descriptions[index])),
                    if (index == 0)
                      FilledButton(
                        onPressed: () {},
                        child: const Text('Open'),
                      ),
                  ],
                ),
              ),
            );
          },
        );
      },
    );
  }
}
